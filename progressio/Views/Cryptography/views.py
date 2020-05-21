from django.http import HttpResponse
from django.shortcuts import render
from progressio.forms import CaesarCipherForm
from progressio.forms import EnigmaMachineForm
from progressio.forms import AffineCipherForm
from progressio.forms import BifidCipherForm
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


def bifidencrypt(request):
	if request.method == 'POST':
		form = BifidCipherForm(request.POST)
		if form.is_valid():
			plaintext = form.cleaned_data.get('input_string')
			key = form.cleaned_data.get('key')
			table = buildpolybiussquare(key)
			form.cleaned_data['output_string'] = bifidencryptmessage(table, plaintext)
			form = BifidCipherForm(form.cleaned_data)
	else:
		form = BifidCipherForm()

	return render(request, GLOBAL_PATH + 'Cryptography/bifidencrypt.html', {'form': form})

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


def buildpolybiussquare(key):
	alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' # I and J are the same for polybius square
	alphabet_list = [char for char in alphabet]

	table = [[0] * 5 for row in range(5)]
	default_table = [[0] * 5 for row in range(5)]

	for x in range(5):
		for y in range(5):
			default_table[x][y] = alphabet[0]
			alphabet = alphabet.replace(alphabet[0], '')
	print(default_table)

	if key is None:
		return default_table
	else:
		key = key.upper()
		for x in range(5):
			for y in range(5):
				try:
					table[x][y] = key[x*5 + y]
					alphabet_list.remove(key[x*5 + y])
				except IndexError:
					table[x][y] = 0

		for x in range(5):
			for y in range(5):
				if table[x][y] == 0:
					table[x][y] = alphabet_list[0]
					del alphabet_list[0]

		return table


def bifidencryptmessage(table, words):
	array = [[0] * len(words) for row in range(2)]
	words = words.upper()
	
	for index in range(len(words)):
		for row in range(len(table)):
			print(table[row])
			if words[index] in table[row]:
				print(words[index])
				array[0][index] += row
				array[1][index] += table[row].index(words[index])

	ciphertext = array[0] + array[1]

	new_text = ''
	coords = list(zip(ciphertext[::2], ciphertext[1::2]))

	for i in coords:
		new_text += str(table[i[0]][i[1]])

	return new_text