from django.shortcuts import render
# i add a not response if not moth
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


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
