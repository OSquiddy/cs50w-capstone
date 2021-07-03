import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.middleware.csrf import get_token


from .models import User, Doctor, Patient
from .serializers import *

# Create your views here.
def frontend(request):
    return HttpResponse(render(request, 'vue_index.html'))

# def token(request):
#     token = get_token(request)
#     return JsonResponse({'token': token})

@ensure_csrf_cookie
def set_csrf_token(request):
    return JsonResponse({'details': 'CSRF Token Cookie has been set'})

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        #Attempt to sign user in
        print(request)
        print('Post request sent')
        data = json.loads(request.body)
        print('Data:', data)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        
        #Check if authentication is successful
        if user is not None:
            login(request, user)
            print("Something is happening")
            return JsonResponse({
                "message": "Login successful",
                "username": username 
                }, status=200)
        else:
            return JsonResponse({"error": "Incorrect credentials"}, status=400)



