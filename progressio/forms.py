from progressio.validators import *


class BaseForm(forms.Form):
	input_string = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}))
	output_string = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 5, "readonly": True}))


# Since crypto is harder in other alphabets, we should extend this class that has the validator_string_is_english method
# for encryption/decryption forms until we extend functionality to other alphabets
class CryptoForm(BaseForm):
	input_string = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}), validators=[validator_string_is_english])


class StringForm(BaseForm):
	pass


class StringParameterForm(BaseForm):
	input_parameter = forms.CharField(widget=forms.Textarea(attrs={"rows": 1}))


class StringHexInputForm(BaseForm):
	input_string = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}), validators=[validator_hex_value])
	output_string = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 5, "readonly": True}))


class StringRGBInputForm(BaseForm):
	input_red = forms.IntegerField(widget=forms.Textarea(attrs={"rows": 1}))
	input_green = forms.IntegerField(widget=forms.Textarea(attrs={"rows": 1}))
	input_blue = forms.IntegerField(widget=forms.Textarea(attrs={"rows": 1}))
	output_string = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 5, "readonly": True}))


class CaesarCipherForm(CryptoForm):
	CAESAR_CIPHER_AVAILABLE_SHIFTS = [
		(1, 1), (2, 2),
		(3, 3), (4, 4),
		(5, 5), (6, 6),
		(7, 7), (8, 8),
		(9, 9), (10, 10),
		(11, 11), (12, 12),
		(13, 13), (14, 14),
		(15, 15), (16, 16),
		(17, 17), (18, 18),
		(19, 19), (20, 20),
		(21, 21), (22, 22),
		(23, 23), (24, 24),
	]

	shift = forms.ChoiceField(choices=CAESAR_CIPHER_AVAILABLE_SHIFTS)


class EnigmaMachineForm(BaseForm):
	WHEEL_NAMES = [
		('IC', 'IC'), ('IIC', 'IIC'),
		('IIIC', 'IIIC'), ('IR', 'IR'),
		('IIR', 'IIR'), ('IIIR', 'IIIR'),
		('UKW', 'UKW'), ('I-K', 'I-K'),
		('II-K', 'II-K'), ('III-K', 'III-K'),
		('UKW-K', 'UKW-K'), ('I', 'I'),
		('II', 'II'), ('III', 'III'),
		('IV', 'IV'), ('V', 'V'),
		('VI', 'VI'), ('VII', 'VII'),
		('VIII', 'VIII'), ('Beta', 'Beta'),
		('Gamma', 'Gamma')
	]

	REFLECTOR_NAMES = [
		('Reflector A', 'Reflector A'),
		('Reflector B', 'Reflector B'),
		('Reflector C', 'Reflector C')
	]

	RING_SETTINGS = [
		('A', 'A'), ('B', 'B'),
		('C', 'C'), ('D', 'D'),
		('E', 'E'), ('F', 'F'),
		('G', 'G'), ('H', 'H'),
		('I', 'I'), ('J', 'J'),
		('K', 'K'), ('L', 'L'),
		('M', 'M'), ('N', 'N'),
		('O', 'O'), ('P', 'P'),
		('Q', 'Q'), ('R', 'R'),
		('S', 'S'), ('T', 'T'),
		('U', 'U'), ('V', 'V'),
		('W', 'W'), ('X', 'X'),
		('Y', 'Y'), ('Z', 'Z')
	]

	wheel = forms.ChoiceField(choices=WHEEL_NAMES)
	ringsetting = forms.ChoiceField(choices=RING_SETTINGS)

	plugboard = forms.CharField(widget=forms.Textarea(attrs={"rows": 1}))
	reflectors = forms.ChoiceField(choices=REFLECTOR_NAMES)


class AffineCipherForm(BaseForm):
	slope = forms.CharField()
	intercept = forms.CharField()


class BifidCipherForm(BaseForm):
	key = forms.CharField(validators=[validator_no_duplicates, validator_no_more_than_26_characters])


class HashFunctionForm(BaseForm):
	HASH_FUNCTION_CHOICES = [
		('sha-1', 'SHA-1'),
		('sha-256', 'SHA-256'),
		('sha-384', 'SHA-384'),
		('sha-512', 'SHA-512'),
		('md5', 'MD5')
	]

	hash = forms.ChoiceField(choices=HASH_FUNCTION_CHOICES)


class HmacForm(BaseForm):
	hash = forms.ChoiceField(choices=HashFunctionForm.HASH_FUNCTION_CHOICES)
	key = forms.CharField()


class TapForm(BaseForm):
	TAP_CHOICES = [
		('.', '.'),
		('-', '-'),
		('_', '_'),
		('*', '*')
	]

	tap = forms.ChoiceField(choices=TAP_CHOICES)


class RC4Form(BaseForm):
	key = forms.CharField()


class AesForm(BaseForm):
	AES_BLOCK_SIZES = [
		('aes-128', 'AES-128'),
		('aes-192', 'AES-192'),
		('aes-256', 'AES-256')
	]

	mode = forms.ChoiceField(choices=AES_BLOCK_SIZES)
	key = forms.CharField()

	def clean(self):
		cleaned_data = super().clean()
		mode = cleaned_data.get('mode')
		key = cleaned_data.get('key')
		print(mode)
		if mode == 'aes-128' and len(key) > 16:
			msg = 'Key length cannot be more than 16 bytes'
			self.add_error('key', msg)
			raise forms.ValidationError('Key length cannot be more than 16 bytes')
		elif mode == 'aes-192' and len(key) > 24:
			msg = 'Key length cannot be more than 24 bytes'
			self.add_error('key', msg)
			raise forms.ValidationError('Key length cannot be more than 24 bytes')
		elif mode == 'aes-256' and len(key) > 32:
			msg = 'Key length cannot be more than 32 bytes'
			self.add_error('key', msg)
			raise forms.ValidationError('Key length cannot be more than 32 bytes')
