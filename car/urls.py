from django.contrib import admin
from django.urls import path,include
from car import views



urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("service", views.service, name='service'),
    path("gallery", views.gallery, name='gallery'),
    path("general", views.general, name='general'),
    path("cardenting", views.cardenting, name='cardenting'),
    path("carwashing", views.carwashing, name='carwashing'),
    path("customrepairing", views.customrepairing, name='customrepairing'),
    path("wheelcare", views.wheelcare, name='wheelcare'),
    path("numberplating", views.numberplating, name='numberplating'),
    path("Privacypolicy", views.Privacypolicy, name='Privacypolicy'),
    path("Termandcondition", views.Termandcondition, name='Termandcondition'),
 
 
 
   
]