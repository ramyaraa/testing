from django.shortcuts import render
# i add a not response if not moth
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# create a dictionary for easying data

monthly_challenges = {
    "january": "1 xot fery HTML bka",
    "february": "2 xot fery CSS bka",
    "march": "3 xot fery JavaScript bka",
    "april": "4 xot fery React bka",
    "may": "5 xot fery Node.js bka",
    "june": "6 xot fery Express.js bka",
    "july": "7 xot fery MongoDB bka",
    "august": "8 xot fery Python bka",
    "september": "9 xot fery Flask bka",
    "october": "10 xot fery Django bka",
    "november": "11 xot fery Git bka",
    "december": "12 xot fery testing and deployment bka"
}

# in here use the dictnary and .keys


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    # if month > len(months):
    if month not in range(1, 13):
        return HttpResponseNotFound("<h1>to kaseke baralay</h1>")
    Redirect_month = months[month-1]
    return HttpResponseRedirect("/monthly/" + Redirect_month)

# use dictnary and pass the parammetars


def monthly_challenge(request, month):
    try:
        text_ka = monthly_challenges[month]
        return HttpResponse(text_ka)
    except:
        return HttpResponseNotFound("<h1>to kaseke baralay</h1>")
