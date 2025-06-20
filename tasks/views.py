from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse("WelCome To Task Management System ")

def contact(request):
    return HttpResponse("<h1 style= 'color:Green'> This Is Contact Page <h1>")

def show_task(request):
    return HttpResponse(" <h1>This Is Our TaskS Page <h1>")


def new_task(request):
    return HttpResponse("This Is New Task And It Create Friday")

def create_task(request):
    return HttpResponse ("Create URLA")