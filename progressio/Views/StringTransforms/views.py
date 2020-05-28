from django.http import HttpResponse
from django.shortcuts import render
from progressio.forms import *
import progressio.context_processor as context

GLOBAL_PATH = 'progressio/'


def index(request):
	return render(request, GLOBAL_PATH + 'index.html')


def string_basic_manipulation(request):
	context.title = 'String Basic Manipulation'

	if request.method == 'POST':
		form = StringForm(request.POST)
		if form.is_valid():
			if request.POST.get('operation') == 'Uppercase':
				form.cleaned_data['output_string'] = form.cleaned_data.get('input_string').upper()
			elif request.POST.get('operation') == 'Lowercase':
				form.cleaned_data['output_string'] = form.cleaned_data.get('input_string').lower()
			elif request.POST.get('operation') == 'Reverse':
				form.cleaned_data['output_string'] = form.cleaned_data.get('input_string')[::-1]
			form = StringForm(form.cleaned_data)
	else:
		form = StringForm()

	return render(request, GLOBAL_PATH + 'StringTransforms/stringbasicmanipulation.html', {'form': form})


def string_length(request):
	context.title = 'String Length'

	if request.method == 'POST':
		form = StringForm(request.POST)
		if form.is_valid():
			form.cleaned_data['output_string'] = len(form.cleaned_data.get('input_string'))
			form = StringForm(form.cleaned_data)
	else:
		form = StringForm()

	return render(request, GLOBAL_PATH + 'StringTransforms/stringlength.html', {'form': form})


def substring_occurrence(request):
	context.title = 'String Occurrence'

	if request.method == 'POST':
		form = StringParameterForm(request.POST)
		if form.is_valid():
			form.cleaned_data['output_string'] = form.cleaned_data.get('input_string').count(
				form.cleaned_data.get('input_parameter'))
			form = StringParameterForm(form.cleaned_data)
	else:
		form = StringParameterForm()

	return render(request, GLOBAL_PATH + 'StringTransforms/substringoccurence.html', {'form': form})


def word_counter(request):
	context.title = 'Word Counter'

	if request.method == 'POST':
		form = StringForm(request.POST)
		if form.is_valid():
			input_text = form.cleaned_data.get('input_string')
			form.cleaned_data['output_string'] = count_words_in_string(input_text)
			form = StringForm(form.cleaned_data)
	else:
		form = StringForm()

	return render(request, GLOBAL_PATH + 'StringTransforms/wordcounter.html', {'form': form})


'''
HELPER FUNCTIONS
'''


def count_words_in_string(input_text):
	for char in '-.,\n':
		input_text = input_text.replace(char, ' ')
	input_text = input_text.lower()
	return len(input_text.split())
