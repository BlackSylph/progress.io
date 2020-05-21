from django.http import HttpResponse
from django.shortcuts import render
from progressio.forms import *

GLOBAL_PATH = 'progressio/'


def index(request):
    return render(request, GLOBAL_PATH + 'index.html')


def stringuppercase(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = form.cleaned_data.get('input_string').upper()
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'StringTransforms/stringuppercase.html', {'form': form})


def stringlowercase(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = form.cleaned_data.get('input_string').lower()
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'StringTransforms/stringlowercase.html', {'form': form})


def stringlength(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = len(form.cleaned_data.get('input_string'))
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'StringTransforms/stringlength.html', {'form': form})


def stringreverse(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = form.cleaned_data.get('input_string')[::-1]
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'StringTransforms/stringreverse.html', {'form': form})


def substringoccurrence(request):
    if request.method == 'POST':
        form = StringParameterForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = form.cleaned_data.get('input_string').count(form.cleaned_data.get('input_parameter'))
            form = StringParameterForm(form.cleaned_data)
    else:
        form = StringParameterForm()

    return render(request, GLOBAL_PATH + 'StringTransforms/substringoccurence.html', {'form': form})


def wordcounter(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            for char in '-.,\n':
                input_text = form.cleaned_data.get('input_string').replace(char, ' ')
            input_text = input_text.lower()
            form.cleaned_data['output_string'] = len(input_text.split())
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'StringTransforms/wordcounter.html', {'form': form})