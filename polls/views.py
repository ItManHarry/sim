from django.shortcuts import render
from django.http import HttpResponse
def demo(request, year):
    return HttpResponse('<h1>OK. The year is '+str(year)+'</h1>')