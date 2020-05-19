from django.http import HttpResponse
from django.shortcuts import render
from progressio.forms import StringForm

GLOBAL_PATH = 'progressio/'


def index(request):
    return render(request, GLOBAL_PATH + 'index.html')


def stringLength(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StringForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.cleaned_data['string_length'] = len(form.cleaned_data.get('input_string'))
            # Update the form with the calculation result.
            form = StringForm(form.cleaned_data)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'Strings/stringlength.html', {'form': form})
