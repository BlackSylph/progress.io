from django import forms


def validator_hex_value(value):
    count = len(value.lstrip('#'))
    if count < 6 or count % 3 != 0:
        raise forms.ValidationError('Wrong hex value')


def validator_rgb_value(value):
    if value < 0 or value > 255:
        raise forms.ValidationError('Wrong RGB value')