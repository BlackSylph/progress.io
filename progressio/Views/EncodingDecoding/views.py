from django.http import HttpResponse
from django.shortcuts import render
from progressio.forms import StringForm
import base64

GLOBAL_PATH = 'progressio/'


def base64encode(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            b64 = form.cleaned_data.get('input_string').encode('ascii')
            b64 = base64.b64encode(b64)
            form.cleaned_data['output_string'] = b64.decode('ascii')
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/base64encode.html', {'form': form})


def base64decode(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            b64 = form.cleaned_data.get('input_string').encode('ascii')
            b64 = base64.b64decode(b64)
            form.cleaned_data['output_string'] = b64.decode('ascii')
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/base64decode.html', {'form': form})


def base32encode(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            b32 = form.cleaned_data.get('input_string').encode('ascii')
            b32 = base64.b32encode(b32)
            form.cleaned_data['output_string'] = b32.decode('ascii')
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/base32encode.html', {'form': form})


def base32decode(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            b32 = form.cleaned_data.get('input_string').encode('ascii')
            b32 = base64.b32decode(b32)
            form.cleaned_data['output_string'] = b32.decode('ascii')
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/base32decode.html', {'form': form})
