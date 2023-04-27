from django.shortcuts import render

from datetime import datetime

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('Welcome to Little Lemon Resturant')

def homepage(request):
    return HttpResponse('Welcome to homepage')

def display_date (request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text="""<h1 style="color: #f4CE14;">This is Little Lemon Website"""
    return HttpResponse(text)