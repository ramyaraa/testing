from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# import the HttpRequest, create a def and return the request


def january(request):
    return HttpResponse('thsi moth is january')


def monthly_challenge(request, month):
    text_ka = None
    if month == "january":
        text_ka = "1 xot fery HTML bka"
    elif month == "februay":
        text_ka = "2 xot fery CSS bka"
    elif month == "march":
        text_ka = "3 xot fery js bka"
    else:
        return HttpResponseNotFound("this month is not found")
    return HttpResponse(text_ka)
