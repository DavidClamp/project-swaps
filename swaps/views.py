from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def my_swaps(request):
    return HttpResponse("Hello, swaps!")
