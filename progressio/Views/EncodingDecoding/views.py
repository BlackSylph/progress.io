from django.shortcuts import render
from progressio.forms import StringForm, StringHexInputForm, StringRGBInputForm
import base64
import binascii
import html.parser
import urllib.parse

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


def htmlencode(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = html.escape(form.cleaned_data.get('input_string'))
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/htmlencode.html', {'form': form})


def htmldecode(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = html.unescape(form.cleaned_data.get('input_string'))
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/htmldecode.html', {'form': form})


def urlencode(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = urllib.parse.quote(form.cleaned_data.get('input_string'), safe='')
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/urlencode.html', {'form': form})


def urldecode(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = urllib.parse.unquote(form.cleaned_data.get('input_string'))
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/urldecode.html', {'form': form})


def decimaltobinary(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = bin(int(form.cleaned_data.get('input_string')))[2:]
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/urldecode.html', {'form': form})


def binarytodecimal(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = int(form.cleaned_data.get('input_string'), 2)
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/urldecode.html', {'form': form})


def decimaltohex(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = hex(int(form.cleaned_data.get('input_string')))
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/urldecode.html', {'form': form})


def hextodecimal(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = int(form.cleaned_data.get('input_string'), 0)
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/urldecode.html', {'form': form})


def hextorgb(request):
    if request.method == 'POST':
        form = StringHexInputForm(request.POST)
        if form.is_valid():
            input_string = form.cleaned_data.get('input_string').lstrip('#')
            lv = len(input_string)
            tup = tuple(int(input_string[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
            form.cleaned_data['output_string'] = ''.join(map(str, tup))
            form = StringHexInputForm(form.cleaned_data)
    else:
        form = StringHexInputForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/hextorgb.html', {'form': form})


def rgbtohex(request):
    if request.method == 'POST':
        form = StringRGBInputForm(request.POST)
        if form.is_valid():
            input_red = form.cleaned_data.get('input_red')
            input_green = form.cleaned_data.get('input_green')
            input_blue = form.cleaned_data.get('input_blue')
            rgb = (input_red, input_green, input_blue)
            form.cleaned_data['output_string'] = '#%02x%02x%02x' % rgb
            form = StringRGBInputForm(form.cleaned_data)
    else:
        form = StringRGBInputForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/rgbtohex.html', {'form': form})
