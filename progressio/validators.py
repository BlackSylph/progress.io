from django import forms
from typing import Final


# Since Python does not support an actual const data type, we kind of enforce it through the Final variable annotation
# for static type checkers and consistency
ONLY_LATIN_CHARACTERS_MSG: Final = 'We currently support encoding/decoding with only latin characters'
WRONG_HEX_VALUE_MSG: Final = 'Wrong hex value'
WRONG_RGB_VALUE_MSG: Final = 'Wrong RGB value'
KEY_NO_DUPLICATES_MSG: Final = 'Key cannot contain duplicate characters'
KEY_NO_MORE_THAN_26_CHARACTERS_MSG: Final = 'Key cannot contain more than 26 characters'


def validator_string_is_english(value):
	try:
		value.encode(encoding='utf-8').decode('ascii')
	except UnicodeDecodeError:
		raise forms.ValidationError(ONLY_LATIN_CHARACTERS_MSG)


def validator_hex_value(value):
	count = len(value.lstrip('#'))
	if count < 6 or count % 3 != 0:
		raise forms.ValidationError(WRONG_HEX_VALUE_MSG)


def validator_rgb_value(value):
	if value < 0 or value > 255:
		raise forms.ValidationError(WRONG_RGB_VALUE_MSG)


def validator_no_duplicates(value):
	if len(set(value)) != len(value):
		raise forms.ValidationError(KEY_NO_DUPLICATES_MSG)


def validator_no_more_than_26_characters(value):
	if len(value) > 26:
		raise forms.ValidationError(KEY_NO_MORE_THAN_26_CHARACTERS_MSG)
