from django.http import HttpResponse
from django.shortcuts import render
from progressio.forms import StringForm

GLOBAL_PATH = 'progressio/'


def index(request):
    return render(request, GLOBAL_PATH + 'index.html')


def stringLength(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = len(form.cleaned_data.get('input_string'))
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'Strings/stringlength.html', {'form': form})

def stringReverse(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            form.cleaned_data['output_string'] = form.cleaned_data.get('input_string')[::-1]
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'Strings/stringreverse.html', {'form': form})
