from time import strftime
from random import randint
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
from django.utils.dateparse import parse_date

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

