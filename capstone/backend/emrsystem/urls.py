from django.urls import path, include

from . import views

vue_urls = [
    # path('', views.frontend),
]

urlpatterns = [
    # path("", views.index, name="index"),
    path("hello", views.hello_world, name="hello"),
    path("userList", views.users, name="users"),
    path("patientList", views.patients, name="patients"),
    path("p/<int:id>", views.patientInfo, name="patientInfo"),
    path("p/<int:id>/v/<int:visitNumber>", views.getReport, name="report"),
    # path('', include(vue_urls)),
    
    # api urls
 ]