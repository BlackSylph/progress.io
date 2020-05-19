from django.http import HttpResponse
from django.shortcuts import render
from progressio.forms import StringForm
import base64
import binascii

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


def stringtohex(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            hex_value = binascii.hexlify(str.encode(form.cleaned_data.get('input_string')))
            form.cleaned_data['output_string'] = hex_value.decode()
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/stringtohex.html', {'form': form})


def hextostring(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = bytearray.fromhex(form.cleaned_data.get('input_string')).decode()
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/stringtohex.html', {'form': form})


def stringtobinary(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = ' '.join(f"{ord(i):08b}" for i in form.cleaned_data.get('input_string'))
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/stringtobinary.html', {'form': form})


def binarytostring(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            bindata = form.cleaned_data.get('input_string')
            binary_values = bindata.split()
            ascii_string = ""

            for binary_value in binary_values:
                an_integer = int(binary_value, 2)
                ascii_character = chr(an_integer)
                ascii_string += ascii_character

            form.cleaned_data['output_string'] = ascii_string
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/binarytostring.html', {'form': form})