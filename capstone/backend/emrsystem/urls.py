from django.urls import path, include

from . import views

vue_urls = [
    # path('', views.frontend),
]

urlpatterns = [
    # path("", views.index, name="index"),
    path("hello", views.hello_world, name="hello"),
    path("userList", views.users, name="users"),
    path("patientList/<str:orderBy>", views.patients, name="patients"),
    path("doctorList/", views.doctors, name="doctors"),
    path("patientList/<str:orderBy>/<str:query>", views.filteredPatients, name="filteredPatients"),
    path("p/<int:id>", views.patientInfo, name="patientInfo"),
    path("d/<int:id>", views.doctorInfo, name="doctorInfo"),
    path("p/<int:id>/v/<int:visitNumber>", views.getReport, name="report"),
    path("appointmentsList", views.appointmentsList, name="appointmentsList"),
    path("appointmentsList/<str:query>", views.filteredAppointments, name="filteredAppointments"),
    path("numPatients", views.numPatients, name="numPatients"),
    path("lastPatient", views.lastPatient, name="lastPatient"),
    path("getEarnings", views.getEarnings, name="getEarnings"),
    path("getEarnings/m", views.getEarningsByMonth, name="getEarningsByMonth"),
    path("createReport/<int:patient_id>/visit/<int:visitNumber>", views.createReport, name="createReport"),
    path("getNumReports/<int:patientID>", views.getNumReports, name="getNumReports"),
    path("createAppointment/<int:patientID>/<int:doctorID>", views.appointment, name="createAppointment"),
    path("uploadImage", views.uploadImage, name="uploadImage"),
    path('create/p', views.createPatient, name="createPatient"),
    path('history/<int:id>', views.pastHistory, name="pastHistory"),
    path('updateUser', views.updateUser, name="updateUser"),
    # path('', include(vue_urls)),
    
    # api urls
 ]