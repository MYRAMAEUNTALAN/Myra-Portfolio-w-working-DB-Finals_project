from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path("",views.HomePage, name = "HomePage"), 
    path("About/",views.About, name = "About"),
    path("Experiences/",views.Experiences, name = "Experiences"), 
    path("Achievements/",views.Achievements, name = "Achievements"),
    path("Contacts/",views.Contacts, name = "Contacts")
]
