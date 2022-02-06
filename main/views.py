from django.shortcuts import render
from django.http import HttpResponse
import os

def usermode(request):
    return render(request, 'main/main.html')
