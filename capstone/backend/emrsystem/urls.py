from django.urls import path, include

from . import views

vue_urls = [
    # path('', views.frontend),
]

urlpatterns = [
    # path("", views.index, name="index"),
    path("hello", views.hello_world, name="hello"),
    path("userList", views.users, name="users"),
    # path('', include(vue_urls)),
    
    # api urls
 ]