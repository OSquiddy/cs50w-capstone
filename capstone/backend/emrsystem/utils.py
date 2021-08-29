from .models import *
from datetime import date, timedelta
from django.db.models import Q

def getAppointmentsList(appointments):
    today = date.today()
    tomorrow = date.today() + timedelta(days=1)
    appointmentsList = []
    if appointments:
        prevDay = appointments[0].date
        patientsList = []
        customData = {}
        key = 0
        obj = {}
        obj['key'] = key
        for appt in appointments:
            day = appt.date
            if prevDay != day:
                appointmentsList.append(obj)
                obj = {}
                key += 1
                obj['key'] = key
                obj['dates'] = day
                customData = {}
                patientsList = []
            appointment = {}
            appointment['id'] = appt.patient.id
            appointment['name'] = f"{appt.patient.fullname()}"
            appointment['time'] = f"{appt.time_from.strftime('%I:%M %p')} - {appt.time_till.strftime('%I:%M %p')}"
            patientsList.append(appointment)
            customData['patientsList'] = patientsList
            if day == today:
                customData['meta'] = 'Today'
            elif day == tomorrow:
                customData['meta'] = 'Tomorrow'
            else:
                customData['meta'] = day.strftime('%A')
            obj['dates'] = day
            obj['customData'] = customData
            prevDay = day
        if len(obj):
            appointmentsList.append(obj)
    return appointmentsList

def getAppointmentsByPartialDigits(query):
    appointments = Visit.objects.filter(Q(patient_id=query) | Q(date__day=query) | Q(date__month=query) | Q(date__year=query)).order_by('date')
    appointmentsList = getAppointmentsList(appointments)
    return appointmentsList

def getAppointmentsByName(query):
    appointments = Visit.objects.filter(Q(patient__first_name__icontains=query) | Q(patient__last_name__icontains=query)).order_by('date', 'time_from')
    appointmentsList = getAppointmentsList(appointments)
    return appointmentsList

def getAppointmentsByDate(query):
    appointments = Visit.objects.filter(date=query).order_by('time_from')
    appointmentsList = getAppointmentsList(appointments)
    return appointmentsList

# def multiDayAppointments(appointments):
#     today = date.today()
#     tomorrow = date.today() + timedelta(days=1)
#     try:
#         prevDay = appointments[0].date
#     except Exception:
#         pass
#     appointmentsList = []
#     patientsList = []
#     customData = {}
#     key = 0
#     for i, appt in enumerate(appointments):
#         print(appt)
#         day = appt.date
#         if prevDay != day:
#             print('This is the way')
#             obj = {}
#             obj['key'] = key
#             key += 1
#             obj['dates'] = prevDay
#             customData['patientsList'] = patientsList
#             if prevDay == today:
#                 customData['meta'] = 'Today'
#             elif prevDay == tomorrow:
#                 customData['meta'] = 'Tomorrow'
#             else:
#                 customData['meta'] = prevDay.strftime('%A')
#             obj['customData'] = customData
#             appointmentsList.append(obj)
#             customData = {}
#             patientsList = []
#         appointment = {}
#         appointment['id'] = appt.patient.id
#         appointment['name'] = f"{appt.patient.fullname()}"
#         appointment['time'] = f"{appt.time_from.strftime('%I:%M %p')} - {appt.time_till.strftime('%I:%M %p')}"
#         patientsList.append(appointment)
#         prevDay = day
#     return appointmentsList

#     def singleDayAppointments(appointments):
#     today = date.today()
#     tomorrow = date.today() + timedelta(days=1)
#     appointmentsList = []
#     if appointments:
#         prevDay = appointments[0].date
#         patientsList = []
#         customData = {}
#         key = 0
#         obj = {}
#         obj['key'] = key
#         for appt in appointments:
#             appointment = {}
#             appointment['id'] = appt.patient.id
#             appointment['name'] = f"{appt.patient.fullname()}"
#             appointment['time'] = f"{appt.time_from.strftime('%I:%M %p')} - {appt.time_till.strftime('%I:%M %p')}"
#             patientsList.append(appointment)
#         customData['patientsList'] = patientsList
#         if prevDay == today:
#             customData['meta'] = 'Today'
#         elif prevDay == tomorrow:
#             customData['meta'] = 'Tomorrow'
#         else:
#             customData['meta'] = prevDay.strftime('%A')
#         obj['customData'] = customData
#         appointmentsList.append(obj)
#     return appointmentsList