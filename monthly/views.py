from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# import the HttpRequest, create a def and return the request


def january(request):
    return HttpResponse('thsi moth is january')


def february(request):
    return HttpResponse("this month is february")


def monthly_challenge():
    return HttpResponse()
