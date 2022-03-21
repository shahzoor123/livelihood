from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'dashboard/index.html')


def login(request):
    return render(request, 'dashboard/registration/login.html')


def signup(request):
    return render(request, 'dashboard/registration/signup.html')


def contactus(request):
    return render(request, 'dashboard/contactus.html')


def search(request):
    return render(request, 'dashboard/search.html')


def calender(request):
    return render(request, 'dashboard/calender.html')

def chart(request):
    return render(request, 'dashboard/chart.html')


def chart2(request):
    return render(request, 'dashboard/chart2.html')    

