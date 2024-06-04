# import path package
from django.urls import path

# import views becaus we wanna work with the index function ,,,, (from .)  it meanse same folder tha urls.py had it
from . import views

# create a list that contain paths
urlpatterns = [
    # this path contain tow argumets , mean if a request reach january  excute index function
    # 1. describe url we wanna support   2. the function we wanna call
    path("january", views.january),
    path("february", views.february),
    path("<month>", views.monthly_challenge)
]
