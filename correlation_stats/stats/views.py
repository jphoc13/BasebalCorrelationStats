from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    "This view needs to call the models or apps.py to do the business logic?"
    return HttpResponse("Hello, world. You're at the stats index.")