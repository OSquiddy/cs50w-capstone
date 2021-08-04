from time import strftime
from warnings import catch_warnings
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from datetime import date, datetime, timedelta
from django.utils import timezone

from .models import *
from .serializers import *

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
def patients(request):
    patientList = Patient.objects.all().order_by('first_name')
    serializer = PatientSerializer(patientList, many=True)
    return Response({"patientList": serializer.data})

@api_view(['GET', 'POST'])
def filteredPatients(request, query):
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
def getReport(request, id, visitNumber):
    patient = Patient.objects.get(id=id)
    print(patient)
    try:
        examination = Examination.objects.get(visit__patient=id, visit__visit_number=visitNumber)
        examinationSerializer = ExaminationSerializer(examination)
        examination = examinationSerializer.data
    except ObjectDoesNotExist:
        examinationSerializer = {}
        examination = examinationSerializer
    
    try:
        pastHistory = PastHistory.objects.get(visit__patient=id, visit__visit_number=visitNumber)
        pastHistorySerializer = PastHistorySerializer(pastHistory)
        pastHistory = pastHistorySerializer.data
    except ObjectDoesNotExist:
        pastHistorySerializer = {}
        pastHistory = pastHistorySerializer

    if patient.sex == 'f':
        try:
            gynecHistory = GynecHistory.objects.get(visit__patient=id, visit__visit_number=visitNumber)
            gynecHistorySerializer = GynecHistorySerializer(gynecHistory)
            gynecHistory = gynecHistorySerializer.data
        except ObjectDoesNotExist:
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
    lastAppointment = Visit.objects.all().order_by('-date').first().date
    today = date.today()
    tomorrow = date.today() + timedelta(days=1)
    numDates = lastAppointment - today
    appointmentsList = []
    for i in range(numDates.days + 1):
        day = today + timedelta(days=i)
        # print('day -> ', day.strftime('%b %d, %Y \n'))
        patientsList = []
        visits = Visit.objects.all().filter(date=day).order_by('time_from')
        # print('visits querySet', visits)
        try:
            # visits = VisitSerializer(visits)
            # print('serialized visits', visits)
            for visit in visits:
                appointment = {}
                appointment['id'] = visit.patient.id
                appointment['name'] = f"{visit.patient.fullname()}"
                appointment['time'] = f"{visit.time_from.strftime('%I:%M %p')} - {visit.time_till.strftime('%I:%M %p')}"
                patientsList.append(appointment)
            obj = {}
            obj['date'] = day
            obj['patientsList'] = patientsList
            if day == today:
                obj['meta'] = 'Today'
            elif day == tomorrow:
                obj['meta'] = 'Tomorrow'
            else:
                obj['meta'] = day.strftime('%A')
            appointmentsList.append(obj)
        except AttributeError:
            appointmentsList.append({})
    return Response({ "appointmentsList": appointmentsList })

@api_view(['GET', 'POST'])
def filteredAppointments(request, query):
    # appointments = Visit.objects.all().filter(Q(date__day=query) | Q(date__month=query) | Q(date__year=query)).order_by('date')
    appointments = Visit.objects.all().filter(Q(patient__first_name__icontains=query) | Q(patient__last_name__icontains=query)).order_by('date', 'time_from')
    today = date.today()
    tomorrow = date.today() + timedelta(days=1)
    appointmentsList = []
    try:
        prevDay = appointments[0].date
    except Exception:
        pass
    patientsList = []
    for appt in appointments:
        day = appt.date
        if prevDay != day:
            obj = {}
            obj['date'] = prevDay
            obj['patientsList'] = patientsList
            if prevDay == today:
                obj['meta'] = 'Today'
            elif prevDay == tomorrow:
                obj['meta'] = 'Tomorrow'
            else:
                obj['meta'] = prevDay.strftime('%A')
            appointmentsList.append(obj)
            patientsList = []
        appointment = {}
        appointment['id'] = appt.patient.id
        appointment['name'] = f"{appt.patient.fullname()}"
        appointment['time'] = f"{appt.time_from.strftime('%I:%M %p')} - {appt.time_till.strftime('%I:%M %p')}"
        patientsList.append(appointment)
        prevDay = day

    return Response({ "appointmentsList": appointmentsList })
