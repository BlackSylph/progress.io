from django.http import HttpResponse
from django.shortcuts import render
from progressio.forms import StringForm
import base64
import binascii
import html.parser
import urllib.parse

GLOBAL_PATH = 'progressio/'


def handler404(request, exception):
    return render(request, GLOBAL_PATH + 'Globals/404.html', status=404)


def handler500(request):
    return render(request, GLOBAL_PATH + 'Globals/500.html', status=500)
