from django.http import HttpResponse
from django.shortcuts import render
from progressio.forms import CaesarCipherForm
from progressio.forms import EnigmaMachineForm
from progressio.forms import AffineCipherForm
from python_enigma import enigma
import json

GLOBAL_PATH = 'progressio/'

'''
REQUESTS
'''

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
			wheel = form.cleaned_data.get('wheel')

			with open("progressio/Views/Cryptography/wheels.json", "r") as file:
				all_wheels = json.load(file)

			# wheel = all_wheels[wheel]
			ringsetting = form.cleaned_data.get('ringsetting')

			rotors = [(wheel, ringsetting)]
			print(rotors)
			plaintext = form.cleaned_data.get('input_string')
			plugboard = form.cleaned_data.get('plugboard')
			reflectors = form.cleaned_data.get('reflectors')
			machine = enigma.Enigma(catalog=all_wheels, stecker=plugboard,
									rotors=rotors, reflector=reflectors, operator=True, word_length=5,
									stator="military")
			form.cleaned_data['output_string'] = machine.parse(plaintext)
			form = EnigmaMachineForm(form.cleaned_data)
	else:
		form = EnigmaMachineForm()

	return render(request, GLOBAL_PATH + 'Cryptography/enigmamachine.html', {'form': form})


def affinecipherencrypt(request):
	if request.method == 'POST':
		form = AffineCipherForm(request.POST)
		if form.is_valid():
			plaintext = form.cleaned_data.get('input_string')
			a = int(form.cleaned_data.get('slope'))
			b = int(form.cleaned_data.get('intercept'))
			form.cleaned_data['output_string'] = affine_encrypt(plaintext, [a, b])
			form = AffineCipherForm(form.cleaned_data)
	else:
		form = AffineCipherForm()

	return render(request, GLOBAL_PATH + 'Cryptography/affinecipherencrypt.html', {'form': form})


def affinecipherdecrypt(request):
	if request.method == 'POST':
		form = AffineCipherForm(request.POST)
		if form.is_valid():
			ciphertext = form.cleaned_data.get('input_string')
			a = int(form.cleaned_data.get('slope'))
			b = int(form.cleaned_data.get('intercept'))
			form.cleaned_data['output_string'] = affine_decrypt(ciphertext, [a, b])
			form = AffineCipherForm(form.cleaned_data)
	else:
		form = AffineCipherForm()

	return render(request, GLOBAL_PATH + 'Cryptography/affinecipherencrypt.html', {'form': form})


'''
HELPER FUNCTIONS
'''


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


# Extended Euclidean Algorithm for finding modular inverse
# eg: modinv(7, 26) = 15
def egcd(a, b):
	x, y, u, v = 0, 1, 1, 0
	while a != 0:
		q, r = b // a, b % a
		m, n = x - u * q, y - v * q
		b, a, x, y, u, v = a, r, u, v, m, n
	gcd = b
	return gcd, x, y


def modinv(a, m):
	gcd, x, y = egcd(a, m)
	if gcd != 1:
		return None  # modular inverse does not exist
	else:
		return x % m


# affine cipher encryption function
# returns the cipher text
def affine_encrypt(text, key):
	# C = (a*P + b) % 26
	return ''.join(
		[chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26) + ord('A')) for t in text.upper().replace(' ', '')])


# affine cipher decryption function
# returns original text
def affine_decrypt(cipher, key):
	# P = (a^-1 * (C - b)) % 26
	return ''.join([chr(((modinv(key[0], 26) * (ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher])
