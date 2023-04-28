from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
]


#Mapping URLs with Parameters

urlpatterns = [
    path('dishes/<str:dish>', views.menuitems) #dish=pasta
]