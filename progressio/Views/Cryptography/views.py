from django.http import HttpResponse
from django.shortcuts import render
from progressio.forms import CaesarCipherForm
from progressio.forms import EnigmaMachineForm
from python_enigma import enigma
import json


GLOBAL_PATH = 'progressio/'


def caesarcipher(request):
    if request.method == 'POST':
        form = CaesarCipherForm(request.POST)
        if form.is_valid():
            shift = int(form.cleaned_data.get('shift'))
            plaintext = form.cleaned_data.get('input_string')
            form.cleaned_data['output_string'] = caesarcipherencrypt(plaintext, shift)
            form = CaesarCipherForm(form.cleaned_data)
    else:
        form = CaesarCipherForm()

    return render(request, GLOBAL_PATH + 'Cryptography/caesarcipher.html', {'form': form})


def enigmamachine(request):
    if request.method == 'POST':
        form = EnigmaMachineForm(request.POST)
        if form.is_valid():
            shift = int(form.cleaned_data.get('shift'))
            plaintext = form.cleaned_data.get('input_string')
            form.cleaned_data['output_string'] = caesarcipherencrypt(plaintext, shift)
            form = EnigmaMachineForm(form.cleaned_data)
    else:
        form = EnigmaMachineForm()

    return render(request, GLOBAL_PATH + 'Cryptography/enigmamachine.html', {'form': form})

def caesarcipherencrypt(plaintext, shift):
    result = ""
    # transverse the plain text
    for i in range(len(plaintext)):
        char = plaintext[i]
        # Encrypt uppercase characters in plain text

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result
