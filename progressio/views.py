from django.http import HttpResponse
from django.shortcuts import render

GLOBAL_PATH = 'progressio/'

def index(request):
    return render(request, GLOBAL_PATH + 'index.html')
