from django.shortcuts import render
from progressio.forms import StringForm, StringHexInputForm, StringRGBInputForm
import progressio.context_processor as context
import base64
import binascii
import html.parser
import urllib.parse

GLOBAL_PATH = 'progressio/'


def base_64(request):
    context.title = 'Base64'

    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            b64 = form.cleaned_data.get('input_string').encode('ascii')
            if request.POST.get('operation') == 'Encode':
                b64 = base64.b64encode(b64)
            elif request.POST.get('operation') == 'Decode':
                b64 = base64.b64decode(b64)
            form.cleaned_data['output_string'] = b64.decode('ascii')
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/base64.html', {'form': form})


def base_32(request):
    context.title = 'Base32'

    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            b32 = form.cleaned_data.get('input_string').encode('ascii')
            if request.POST.get('operation') == 'Encode':
                b32 = base64.b32encode(b32)
            elif request.POST.get('operation') == 'Decode':
                b32 = base64.b32decode(b32)
            form.cleaned_data['output_string'] = b32.decode('ascii')
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/base32.html', {'form': form})


def string_to_binary(request):
    context.title = 'String to Binary'

    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = ' '.join(f"{ord(i):08b}" for i in form.cleaned_data.get('input_string'))
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/stringtobinary.html', {'form': form})


def binary_to_string(request):
    context.title = 'Binary to String'

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


def string_to_hex(request):
    context.title = 'String to Hex'

    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            hex_value = binascii.hexlify(str.encode(form.cleaned_data.get('input_string')))
            form.cleaned_data['output_string'] = hex_value.decode()
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/stringtohex.html', {'form': form})


def hex_to_string(request):
    context.title = 'Hex to String'

    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = bytearray.fromhex(form.cleaned_data.get('input_string')).decode()
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/stringtohex.html', {'form': form})


def decimal_to_binary(request):
    context.title = 'Decimal to Binary'

    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = bin(int(form.cleaned_data.get('input_string')))[2:]
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/urldecode.html', {'form': form})


def binary_to_decimal(request):
    context.title = 'Binary to Decimal'

    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = int(form.cleaned_data.get('input_string'), 2)
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/urldecode.html', {'form': form})


def decimal_to_hex(request):
    context.title = 'Decimal to Hex'

    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = hex(int(form.cleaned_data.get('input_string')))
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/urldecode.html', {'form': form})


def hex_to_decimal(request):
    context.title = 'Hex to Decimal'

    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = int(form.cleaned_data.get('input_string'), 0)
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/urldecode.html', {'form': form})


def hex_to_rgb(request):
    context.title = 'Hex to RGB'

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


def rgb_to_hex(request):
    context.title = 'RBG to Hex'

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


def html_encode(request):
    context.title = 'String HTML Encode'

    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = html.escape(form.cleaned_data.get('input_string'))
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/htmlencode.html', {'form': form})


def html_decode(request):
    context.title = 'String HTML Decode'

    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = html.unescape(form.cleaned_data.get('input_string'))
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/htmldecode.html', {'form': form})


def url_encode(request):
    context.title = 'URL Encode'

    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = urllib.parse.quote(form.cleaned_data.get('input_string'), safe='')
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/urlencode.html', {'form': form})


def url_decode(request):
    context.title = 'URL Decode'

    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = urllib.parse.unquote(form.cleaned_data.get('input_string'))
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'EncodingDecoding/urldecode.html', {'form': form})

