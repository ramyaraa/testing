# import path package
from django.urls import path

# import views becaus we wanna work with the index function ,,,, (from .)  it meanse same folder tha urls.py had it
from . import views

# the int ane str before month it fillter it if you type number first function will excute if string second function will excute
urlpatterns = [
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge)
]
