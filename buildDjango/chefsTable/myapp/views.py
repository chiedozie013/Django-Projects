from django.shortcuts import render

from datetime import datetime

# Create your views here.
from django.http import HttpResponse

# def home(request):
#     return HttpResponse('Welcome to Little Lemon Resturant')

def homepage(request):
    response = HttpResponse('Welcome to homepage')
    return response

def display_date (request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text="""<h1 style="color: #f4CE14;">This is Little Lemon Website"""
    return HttpResponse(text)

def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse()
    response.headers['Age'] = 20


# Creating Request and Response
# This is useful in creating forms, working with data bases and other common data structures in django

    msg = f"""<br>
        <br>Path: {path}
        <br>Address: {address}
        <br>Scheme: {scheme}
        <br>Method: {method}
        <br>User agent: {user_agent}
        <br>Path info: {path_info}
        <br>Response header: {response.headers}
    
    """
    return HttpResponse(msg, content_type='text/html', charset='utf-8')


#Mapping URLs with PArameters

def menuitems(request, dish):
    items = {
        'pasta': 'Pasta is a type of noodle from comination of',
        'falafel': 'Falafel are deep fried patties or balls made from',
        'cheesecake': 'Cheesecake is a type of dessert made with cheese'
    }

    description = items[dish]

    return HttpResponse(f"<h2> {dish} <h2>" + description)