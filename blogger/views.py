# Create your views here.

from django.http import HttpResponse


def home():
    return HttpResponse('hey')