from django.shortcuts import render
from django.contrib.auth import login,authenticate
from django.http import HttpResponse
import rest_framework
# Create your views here.

def register(request):
    return HttpResponse("<h1>Account successfully created </h1>")

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
