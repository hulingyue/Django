from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# class Hello(object):
#     pass
def Hello(request):
    return HttpResponse("Hello World")

