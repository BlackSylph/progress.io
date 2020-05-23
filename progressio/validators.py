from django import forms


def validator_hex_value(value):
	count = len(value.lstrip('#'))
	if count < 6 or count % 3 != 0:
		raise forms.ValidationError('Wrong hex value')


def validator_rgb_value(value):
	if value < 0 or value > 255:
		raise forms.ValidationError('Wrong RGB value')


def validator_no_duplicates(value):
	if len(set(value)) != len(value):
		raise forms.ValidationError('Key cannot contain duplicate characters')


def validator_no_more_than_26_characters(value):
	if len(value) > 26:
		raise forms.ValidationError('Key cannot contain more than 26 characters')
