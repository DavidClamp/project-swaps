from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def my_workspace(request):
    return HttpResponse("Hello, workspace!")
