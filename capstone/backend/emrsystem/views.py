from time import strftime
from random import randint
from warnings import catch_warnings
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db.models import Q, functions
from datetime import date, datetime, timedelta
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.utils.translation import gettext as _
import json

from django.shortcuts import render, redirect

from .models import *
from .serializers import *
from .utils import *

# Create your views here.
@api_view(['GET'])
def hello_world(request):
    return Response({ "message": "Hello, world!" })

@api_view(['GET', 'POST'])
def users(request):
    user = UserSerializer(request.user)
    userList = Doctor.objects.all()
    serializer = DoctorSerializer(userList, many=True)
    return Response({ "userList": serializer.data, "current-user": user.data })

@api_view(['GET', 'POST'])
def patients(request, orderBy):
    if orderBy == 'id':
        patientList = Patient.objects.all()
    elif orderBy == 'name':
        patientList = Patient.objects.all().order_by('first_name')
    serializer = PatientSerializer(patientList, many=True)
    return Response({"patientList": serializer.data})

@api_view(['GET'])
def doctors(request):
    doctorList = Doctor.objects.all().order_by('first_name')
    serializer = DoctorSerializer(doctorList, many=True)
    return Response({"doctorList": serializer.data})

@api_view(['GET', 'POST'])
def filteredPatients(request, orderBy, query):
    query = str(query)
    patientList = Patient.objects.filter(Q(first_name__icontains=query) | Q(id__contains=query) | Q(last_name__contains=query)).order_by('first_name')
    serializer = PatientSerializer(patientList, many=True)
    return Response({"patientList": serializer.data})

@api_view(['GET'])
def patientInfo(request, id):
    patientInfo = Patient.objects.get(id=id)
    serializer = PatientSerializer(patientInfo)
    return Response({ "patientInfo": serializer.data })

@api_view(['GET'])
def doctorInfo(request, id):
    doctorInfo = Doctor.objects.get(id=id)
    serializer = DoctorSerializer(doctorInfo)
    return Response({ "doctorInfo": serializer.data })

@api_view(['GET'])
def numPatients(request):
    patients = Patient.objects.all()
    malePatients = patients.filter(sex='M')
    femalePatients = patients.filter(sex='F')
    otherPatients = patients.filter(sex='O')
    numPatients = {
        'male': len(malePatients),
        'female': len(femalePatients),
        'other': len(otherPatients),
        'total': len(patients)
    }
    return Response({ "numPatients": numPatients })

@api_view(['GET'])
def getEarnings(request):
    appointments = Visit.objects.all().order_by('date')
    totalEarnings = 0
    earnings = []
    obj = {}
    obj['value'] = 0
    prevDate = appointments[0].date
    for appt in appointments:
        if appt.visit_completed:
            if appt.date != prevDate:
                earnings.append(obj)
                obj = {}
                obj['value'] = 0
            obj['date'] = appt.date
            obj['value'] += appt.payment
            totalEarnings += appt.payment
            prevDate = appt.date
    # appointments = Visit.objects.all().order_by('date')
    # totalEarnings = 0
    # earnings = []
    # obj = {}
    # obj['value'] = 0
    # prevDate = appointments[0].date
    # obj['date'] = prevDate
    # count = 0
    # for appt in appointments:
    #     if appt.date != prevDate:
    #         # print(appt.date, prevDate)
    #         lastVal = obj['value']
    #         earnings.append(obj)
    #         obj = {}
    #         obj['value'] = lastVal
    #         obj['date'] = appt.date
    #     obj['value'] += appt.payment
    #     prevDate = appt.date
    #     totalEarnings += appt.payment
    earnings.append(obj)
    return Response({ "earnings": totalEarnings, "earningsData": earnings })

@api_view(['GET'])
def getEarningsByMonth(request):
    appointments = Visit.objects.all().order_by('date')
    totalEarnings = 0
    earnings = []
    obj = {}
    obj['value'] = 0
    prevMonth = appointments[0].date.month
    for appt in appointments:
        if appt.visit_completed:
            if appt.date.month != prevMonth:
                earnings.append(obj)
                obj = {}
                obj['value'] = 0
            obj['date'] = appt.date
            obj['value'] += appt.payment
            totalEarnings += appt.payment
            prevMonth = appt.date.month
    earnings.append(obj)
    return Response({ "earnings": totalEarnings, "earningsData": earnings })

@api_view(['GET'])
def lastPatient(request):
    patient = Patient.objects.all().order_by('-date_joined').first()
    serializer = PatientSerializer(patient)
    return Response({ "lastPatient": serializer.data })

@api_view(['GET'])
def getReport(request, id, visitNumber):
    patient = Patient.objects.get(id=id)
    print(patient, 'is a weirdo')
    try:
        print('Trying examination')
        examination = Examination.objects.get(visit__patient=id, visit__visit_number=visitNumber)
        examinationSerializer = ExaminationSerializer(examination)
        examination = examinationSerializer.data
    except Exception:
        print('Failed examination')
        examinationSerializer = {}
        examination = examinationSerializer
    
    try:
        print('Trying pHistory')
        pastHistory = PastHistory.objects.get(visit__patient=id, visit__visit_number=visitNumber)
        pastHistorySerializer = PastHistorySerializer(pastHistory)
        pastHistory = pastHistorySerializer.data
    except Exception:
        print('Failed pHistory')
        pastHistorySerializer = {}
        pastHistory = pastHistorySerializer

    if patient.sex == 'f':
        try:
            gynecHistory = GynecHistory.objects.get(visit__patient=id, visit__visit_number=visitNumber)
            gynecHistorySerializer = GynecHistorySerializer(gynecHistory)
            gynecHistory = gynecHistorySerializer.data
        except Exception:
            gynecHistorySerializer = {}
            gynecHistory = gynecHistorySerializer
    else:
        gynecHistorySerializer = {}
        gynecHistory = gynecHistorySerializer
    
    return Response({ 
        "examination": examination,
        "pastHistory": pastHistory,
        "gynecHistory": gynecHistory
    })
    
@api_view(['GET'])
def appointmentsList(request):
    visits = Visit.objects.all().order_by('date')
    firstAppointment = visits.first().date
    lastAppointment = visits.last().date
    today = date.today()
    tomorrow = date.today() + timedelta(days=1)
    numDates = lastAppointment - firstAppointment
    appointmentsList = []
    colors = ['#1976D2', '#558B2F', '#AD1457', '#7C4DFF', '#C62828', '#004D40' ]
    for i in range(numDates.days + 1):
        day = firstAppointment + timedelta(days=i)
        # print('day -> ', day.strftime('%b %d, %Y \n'))
        patientsList = []
        visits = Visit.objects.filter(date=day).order_by('time_from')
        try:
            for j, visit in enumerate(visits):
                appointment = {}
                appointment['id'] = visit.patient.id
                appointment['name'] = f"{visit.patient.fullname()}"
                appointment['time'] = f"{visit.time_from.strftime('%I:%M %p')} - {visit.time_till.strftime('%I:%M %p')}"
                appointment['background'] = colors[randint(0, len(colors)-1)]
                appointment['visitNumber'] = visit.visit_number
                appointment['visitCompleted'] = visit.visit_completed
                patientsList.append(appointment)
            obj = {}
            obj['key'] = i
            customData = {}
            customData['patientsList'] = patientsList
            # obj['patientsList'] = patientsList
            if day == today:
                customData['meta'] = 'Today'
            elif day == tomorrow:
                customData['meta'] = 'Tomorrow'
            else:
                customData['meta'] = day.strftime('%A')
            obj['customData'] = customData
            obj['dates'] = day
            appointmentsList.append(obj)
        except AttributeError:
            appointmentsList.append({})
    return Response({ "appointmentsList": appointmentsList })

@api_view(['GET', 'POST'])
def filteredAppointments(request, query):
    appointmentsList = []
    if query.isdigit():
        appointmentsList = getAppointmentsByPartialDigits(query)
    elif '-' in query:
        query = parse_date(query)
        appointmentsList = getAppointmentsByDate(query)
    else:
        appointmentsList = getAppointmentsByName(query)
    return Response({ "appointmentsList": appointmentsList })

@api_view(['GET', 'POST'])
def createReport(request, patient_id, visitNumber):
    visit = Visit.objects.get(patient=patient_id, visit_number=visitNumber)
    if request.method == "POST":
        data = json.loads(request.body)
        cardio = data['cardio'] if data['cardio'] is not None else 'NAD'
        cerebero = data['cerebero'] if data['cerebero'] is not None else 'NAD'
        respiratory = data['respiratory'] if data['respiratory'] is not None else 'NAD'
        local_examination = data['localExam'] if data['localExam'] is not None else 'NAD'
        per_abdominal = data['per_abdominal'] if data['per_abdominal'] is not None else 'NAD'
        try:
            examination = Examination.objects.get(visit=visit)
            examination.cardiovascular = cardio
            examination.cereberovascular = cerebero
            examination.respiratory = respiratory
            examination.local_examination = local_examination
            examination.per_abdominal = per_abdominal
            examination.temperature = data['temp']
            examination.pallor = data['pallor']
            examination.pulse_rate = data['pulse']
            examination.blood_pressure = data['bloodPressure']
            examination.SpO2 = data['spo2']
            examination.others = data['others']
            examination.koilonychia = data['koilonychia']
            examination.lymphadenopathy = data['lymphadenopathy']
            examination.clubbing = data['clubbing']
            examination.diagnosis = data['diagnosis']
            examination.oedema = data['oedema']
            examination.icterus = data['icterus']
            examination.complaints = data['complaints']
            examination.save()
        except ObjectDoesNotExist:
            examination = Examination.objects.create(
            visit=visit, blood_pressure=data['bloodPressure'], SpO2=data['spo2'], temperature=data['temp'], respiratory=respiratory, cardiovascular=cardio, cereberovascular=cerebero, others=data['others'], pallor=data['pallor'], pulse_rate=data['pulse'], koilonychia=data['koilonychia'], oedema=data['oedema'], icterus=data['icterus'], lymphadenopathy=data['lymphadenopathy'], clubbing=data['clubbing'], diagnosis=data['diagnosis'], per_abdominal=per_abdominal, local_examination=local_examination, complaints=data['complaints']
            )
        report = generatePDFReport(visit, examination)
        return Response()
    examination = Examination.objects.get(visit=visit)
    report = generatePDFReport(visit, examination)
    return Response()

@api_view(['GET'])
def getNumReports(request, patientID):
    totalCompletedVisits = Visit.objects.filter(patient=patientID, visit_completed=True).order_by('-visit_number')
    serializer = VisitSerializer(totalCompletedVisits, many=True)
    patient = Patient.objects.get(id=patientID)
    patient = PatientSerializer(patient)
    return Response({ "completedVisits": serializer.data, "patient": patient.data })

@api_view(['POST'])
def appointment(request, patientID, doctorID):
    patient = Patient.objects.get(id=patientID)
    doctor = Doctor.objects.get(id=doctorID)
    if request.method == 'POST':
        data = json.loads(request.body)
        print(request.body)
        Visit.objects.create(patient=patient, assigned_doctor=doctor, date=data['date'], time_from=data['time1'], time_till=data['time2'], Unit='01', payment=data['payment'])
    return Response()

@api_view(['POST', 'GET'])
def uploadImage(request):
    user = request.user
    if request.method == 'POST':
        user.profilePic = request.FILES.get('image')
        user.save()
    return Response({ "user": UserSerializer(user).data })

@api_view(['POST'])
def createPatient(request):
    patient = []
    serializer = None
    data = json.loads(request.body)
    response = validateNewPatient(data)
    if isinstance(response, Exception):
        return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return response
    # return Response({ "patient": serializer.data })

        # email, is_active, first_name, last_name, is_staff, date_joined, Phone_Number, address, date_of_birth, isDoctor, isPatient, sex, age, fathers_name, mothers_name, occupation, blood_type, last_visit, patient_type

@api_view(['GET', 'POST'])
def pastHistory(request, id):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            history = PastHistory.objects.get(patient=id)
            history.t2dm = data.get('t2dm')
            history.chronic_kidney_disease = data.get('kidney_disease')
            history.cardiovascular_disease = data.get('cardiovascular_disease')
            history.heart_disease = data.get('heart_disease')
            history.hypothyroidism = data.get('hypothyroidism')
            history.general = data.get('general')
            history.surgeries = data.get('surgeries')
            history.allergies = data.get('allergies')
            history.drugs = data.get('drugs')
            history.family = data.get('family')
            history.save()
        except ObjectDoesNotExist:
            patient = Patient.objects.get(id=id)
            history = PastHistory.objects.create(patient=patient, surgeries=data.get('surgeries'), allergies=data.get('allergies'), general=data.get('general'), drugs=data.get('drugs'), family=data.get('family'), t2dm=data.get('t2dm'), heart_disease=data.get('heart_disease'), hypothyroidism=data.get('hypothyroidism'), cardiovascular_disease=data.get('cardiovascular_disease'), chronic_kidney_disease=data.get('kidney_disease'))
        serializer = PastHistorySerializer(history)
        return Response({ "history": serializer.data })
    else:
        try:
            history = PastHistory.objects.get(patient=id)
            serializer = PastHistorySerializer(history)
            return Response({ "history": serializer.data })
        except ObjectDoesNotExist:
            return Response()

@api_view(['GET', 'POST'])
def updateUser(request):
    print(request.user, request.method)
    user = []
    user = Doctor.objects.get(id=request.user.id)
    serializer = None
    serializer = DoctorSerializer(user)
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        email = data['email']
        sex = data['sex']
        # address = data['address'] + '\n' 
        # + data['city'] if data['city'] else '' + '\n' 
        # + data['state'] if data['state'] else '' + '\n' 
        # + data['zipcode'] if data['zipcode'] else '' + '\n' 
        # + data['country'] if data['country'] else ''
        address = f"{data['address']}\n{data['city'] if data['city'] else ' '}\n{data['state'] if data['state'] else ' '}\n{data['zipcode'] if data['zipcode'] else ' '}\n{data['country'] if data['country'] else ' '}"
        print(address)
        dob = data['dob']
        mob = data['mobile']
        username = data['username']
        try:
            user = Doctor.objects.get(id=request.user.id)
            user.email = email
            user.sex = sex
            user.address = address
            user.date_of_birth = dob
            user.Phone_Number = mob
            user.username = username
            user.save()
            serializer = DoctorSerializer(user)
        except Exception as e:
            print(e)
            return Response({ "errors": e })
    return Response({ "user": serializer.data })