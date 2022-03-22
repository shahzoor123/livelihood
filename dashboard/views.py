from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'dashboard/index.html')


def contactus(request):
    return render(request, 'dashboard/contactus.html')


def search(request):
    return render(request, 'dashboard/search.html')


def calender(request):
    return render(request, 'dashboard/calender.html')

def chart(request):
    return render(request, 'dashboard/chart.html')


def maps(request):
    return render(request, 'dashboard/maps.html')    

def test(request):
    return render(request, 'dashboard/test.html')     

