from django.urls import path, include

from . import views

vue_urls = [
    path('', views.frontend),
]

urlpatterns = [
    # path("", views.index, name="index"),
    # path("login", views.login, name="login"),
    path('', include(vue_urls)),
    
    #api urls
    path('api/login', views.login_view),
]