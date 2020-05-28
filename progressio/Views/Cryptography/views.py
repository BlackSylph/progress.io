from django.shortcuts import render

from progressio.forms import CaesarCipherForm, StringForm, StringParameterForm
from progressio.forms import EnigmaMachineForm
from progressio.forms import AffineCipherForm
from progressio.forms import BifidCipherForm
from progressio.forms import HashFunctionForm
from progressio.forms import HmacForm
from progressio.forms import RC4Form
from progressio.forms import AesForm
from progressio.forms import TapForm

from python_enigma import enigma
# from Crypto.Cipher import ARC4
# from Crypto.Cipher import AES
from secretpy import Trifid, Nihilist, alphabets, CryptMachine
from secretpy.cmdecorators import UpperCase, SaveSpaces, NoSpaces

import hashlib
import hmac as hmac_import
import json
import progressio.context_processor as context

GLOBAL_PATH = 'progressio/'

'''
REQUESTS
'''


def caesar_cipher(request):
    context.title = 'Caesar Cipher'
    if request.method == 'POST':
        form = CaesarCipherForm(request.POST)
        if form.is_valid():
            shift = int(form.cleaned_data.get('shift'))
            plaintext = form.cleaned_data.get('input_string')
            form.cleaned_data['output_string'] = caesar_cipher_encrypt(plaintext, shift)
            form = CaesarCipherForm(form.cleaned_data)
    else:
        form = CaesarCipherForm()

    return render(request, GLOBAL_PATH + 'Cryptography/caesarcipher.html', {'form': form})


def enigma_machine(request):
    context.title = 'Enigma Machine'
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


def affine_cipher(request):
    context.title = 'Affine Cipher'

    if request.method == 'POST':
        form = AffineCipherForm(request.POST)
        if form.is_valid():
            inputtext = form.cleaned_data.get('input_string')
            a = int(form.cleaned_data.get('slope'))
            b = int(form.cleaned_data.get('intercept'))

            if request.POST.get('operation') == 'Encrypt':
                form.cleaned_data['output_string'] = affine_encrypt(inputtext, [a, b])
            elif request.POST.get('operation') == 'Decrypt':
                form.cleaned_data['output_string'] = affine_decrypt(inputtext, [a, b])
            form = AffineCipherForm(form.cleaned_data)
    else:
        form = AffineCipherForm()

    return render(request, GLOBAL_PATH + 'Cryptography/affinecipher.html', {'form': form})


def bifid_cipher(request):
    context.title = 'Bifid Cipher'
    if request.method == 'POST':
        form = BifidCipherForm(request.POST)
        if form.is_valid():
            inputtext = form.cleaned_data.get('input_string')
            key = form.cleaned_data.get('key')
            table = build_polybius_square(key)

            if request.POST.get('operation') == 'Encrypt':
                form.cleaned_data['output_string'] = bifid_encrypt_message(table, inputtext)
            elif request.POST.get('operation') == 'Decrypt':
                form.cleaned_data['output_string'] = bifid_decrypt_message(table, inputtext)
            form = BifidCipherForm(form.cleaned_data)
    else:
        form = BifidCipherForm()

    return render(request, GLOBAL_PATH + 'Cryptography/bifidcipher.html', {'form': form})


def rot13_cipher(request):
    context.title = 'ROT13 Cipher'
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            plaintext = form.cleaned_data.get('input_string')
            form.cleaned_data['output_string'] = caesar_cipher_encrypt(plaintext, 13)
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'Cryptography/rot13cipher.html', {'form': form})


def a1z26_cipher(request):
    context.title = 'A1Z26 Cipher'
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            plaintext = form.cleaned_data.get('input_string')

            if request.POST.get('operation') == 'Encrypt':
                form.cleaned_data['output_string'] = a1z26_encrypt(plaintext)
            elif request.POST.get('operation') == 'Decrypt':
                form.cleaned_data['output_string'] = a1z26_decrypt(plaintext)

            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'Cryptography/a1z26cipher.html', {'form': form})


def vigenere_cipher(request):
    context.title = 'Vigenère Cipher'
    if request.method == 'POST':
        form = StringParameterForm(request.POST)
        if form.is_valid():
            plaintext = form.cleaned_data.get('input_string')
            key = form.cleaned_data.get('input_parameter')

            if request.POST.get('operation') == 'Encrypt':
                form.cleaned_data['output_string'] = vigenere_encrypt(plaintext, key)
            elif request.POST.get('operation') == 'Decrypt':
                form.cleaned_data['output_string'] = vigenere_decrypt(plaintext, key)

            form = StringParameterForm(form.cleaned_data)
    else:
        form = StringParameterForm()

    return render(request, GLOBAL_PATH + 'Cryptography/vigenerecipher.html', {'form': form})


def bacon_cipher(request):
    context.title = 'Bacon Cipher'

    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            inputtext = form.cleaned_data.get('input_string')
            if request.POST.get('operation') == 'Encrypt':
                form.cleaned_data['output_string'] = bacon_encrypt(inputtext)
            elif request.POST.get('operation') == 'Decrypt':
                form.cleaned_data['output_string'] = bacon_decrypt(inputtext)
            form = StringForm(form.cleaned_data)
    else:
        form = StringForm()

    return render(request, GLOBAL_PATH + 'Cryptography/baconcipher.html', {'form': form})


def hash_function(request):
    context.title = 'Hash Function'
    if request.method == 'POST':
        form = HashFunctionForm(request.POST)
        if form.is_valid():
            plaintext = form.cleaned_data.get('input_string')
            func = form.cleaned_data.get('hash')
            form.cleaned_data['output_string'] = hash_based_on_input(func, plaintext)
            form = HashFunctionForm(form.cleaned_data)
    else:
        form = HashFunctionForm()

    return render(request, GLOBAL_PATH + 'Cryptography/hashfunction.html', {'form': form})


def hmac(request):
    context.title = 'HMAC'
    if request.method == 'POST':
        form = HmacForm(request.POST)
        if form.is_valid():
            plaintext = form.cleaned_data.get('input_string')
            func = form.cleaned_data.get('hash')
            key = form.cleaned_data.get('key')
            form.cleaned_data['output_string'] = hmac_based_on_input(func, plaintext, key)
            form = HmacForm(form.cleaned_data)
    else:
        form = HmacForm()

    return render(request, GLOBAL_PATH + 'Cryptography/hmac.html', {'form': form})


def tap_code_cipher(request):
    context.title = 'Tapcode Cipher'
    if request.method == 'POST':
        form = TapForm(request.POST)
        if form.is_valid():
            tap = form.cleaned_data.get('tap')
            table = build_polybius_square(None, 'ABCDEFGHIJLMNOPQRSTUVWXYZ')

            if request.POST.get('operation') == 'Encrypt':
                inputtext = form.cleaned_data.get('input_string').upper()
                form.cleaned_data['output_string'] = tap_code_encrypt(inputtext, table, tap)
            elif request.POST.get('operation') == 'Decrypt':
                inputtext = form.cleaned_data.get('input_string').split(' ')
                form.cleaned_data['output_string'] = tap_code_decrypt(inputtext, table)
            print(form.cleaned_data['output_string'])
            form = TapForm(form.cleaned_data)
    else:
        form = TapForm()

    return render(request, GLOBAL_PATH + 'Cryptography/tapcodecipher.html', {'form': form})


def nihilist_cipher(request):
    context.title = 'Nihilist Cipher'
    if request.method == 'POST':
        form = BifidCipherForm(request.POST)
        if form.is_valid():
            inputtext = form.cleaned_data.get('input_string')
            key = form.cleaned_data.get('key')
            cipher = Nihilist()
            cm = CryptMachine(cipher, key)

            if request.POST.get('operation') == 'Encrypt':
                form.cleaned_data['output_string'] = cm.encrypt(inputtext)
            elif request.POST.get('operation') == 'Decrypt':
                form.cleaned_data['output_string'] = cm.decrypt(inputtext)
            form = BifidCipherForm(form.cleaned_data)
    else:
        form = BifidCipherForm()

    return render(request, GLOBAL_PATH + 'Cryptography/nihilistcipher.html', {'form': form})


def trifid_cipher(request):
    context.title = 'Trifid Cipher'
    if request.method == 'POST':
        form = BifidCipherForm(request.POST)
        if form.is_valid():
            inputtext = form.cleaned_data.get('input_string')
            key = 5
            cipher = Trifid()
            cm = CryptMachine(cipher, key)

            alphabet = [
                u"e", u"p", u"s",
                u"d", u"u", u"c",
                u"v", u"w", u"y",

                u"m", u".", u"z",
                u"l", u"k", u"x",
                u"n", u"b", u"t",

                u"f", u"g", u"o",
                u"r", u"i", u"j",
                u"h", u"a", u"q",
            ]

            cm.set_alphabet(alphabet)
            if request.POST.get('operation') == 'Encrypt':
                form.cleaned_data['output_string'] = cm.encrypt(inputtext)
            elif request.POST.get('operation') == 'Decrypt':
                form.cleaned_data['output_string'] = cm.decrypt(inputtext)
            form = BifidCipherForm(form.cleaned_data)
    else:
        form = BifidCipherForm()

    return render(request, GLOBAL_PATH + 'Cryptography/trifid.html', {'form': form})


# RC4 and AES are wrong, need to recheck
def rc4_cipher(request):
    context.title = 'RC4'
    if request.method == 'POST':
        form = RC4Form(request.POST)  # Use bifid cipher here because both only need an input, key and output string
        if form.is_valid():
            ciphertext = form.cleaned_data.get('input_string').encode()
            key = form.cleaned_data.get('key').encode()
            arc4 = ARC4.new(key)
            form.cleaned_data['output_string'] = arc4.decrypt(ciphertext).hex()
            form = RC4Form(form.cleaned_data)
    else:
        form = RC4Form()

    return render(request, GLOBAL_PATH + 'Cryptography/rc4.html', {'form': form})


def aes(request):
    context.title = 'AES'
    if request.method == 'POST':
        form = AesForm(request.POST)  # Use bifid cipher here because both only need an input, key and output string
        if form.is_valid():
            inputtext = form.cleaned_data.get('input_string').encode()
            key = form.cleaned_data.get('key').encode()
            iv = 'IVIVIVIVIVIVIVIV'
            iv = str.encode(iv)
            aes = AES.new(key, AES.MODE_CBC, iv)

            if request.POST.get('operation') == 'Encrypt':
                inputtext = inputtext + (AES.block_size - (len(inputtext) % AES.block_size)) * b'\x00'
                ciphertext = aes.encrypt(inputtext)
                form.cleaned_data['output_string'] = ciphertext.hex()
            elif request.POST.get('operation') == 'Decrypt':
                form.cleaned_data['output_string'] = aes.decrypt(inputtext).hex()
            form = AesForm(form.cleaned_data)
    else:
        form = AesForm()

    return render(request, GLOBAL_PATH + 'Cryptography/aes.html', {'form': form})


'''
HELPER FUNCTIONS
'''


def tap_code_encrypt(inputtext, table, tap):
    outputtext = ''
    for char in inputtext:

        for i, sub_list in enumerate(table):
            if char in sub_list:
                outputtext += tap * (i + 1)
                outputtext += ' '
                outputtext += tap * (sub_list.index(char) + 1)
                outputtext += ' '

    return outputtext


def tap_code_decrypt(inputtext, table):
    outputtext = ''
    for x, y in pairwise(inputtext):
        outputtext += table[len(x) - 1][len(y) - 1]
    return outputtext


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


def bacon_encrypt(plaintext):
    plaintext = plaintext.lower()  # Format to Lowercase
    plaintext = plaintext.replace('j', 'i')
    plaintext = plaintext.replace('v', 'u')
    ciphertext = ''
    for letter in plaintext:
        bin_value = format(ord(letter) - 97, 'b')
        value = ''
        for i in range(0, 5 - len(bin_value)):
            value += 'a'
        value += bin_value
        value = value.replace('0', 'a')
        value = value.replace('1', 'b')
        ciphertext = ciphertext + ' ' + value
    return ciphertext


def bacon_decrypt(ciphertext):
    ciphertext = ciphertext.lower()  # Format to Lowercase

    # A/B to 0/1 conversion
    plaintext = ciphertext.replace(' ', '')
    plaintext = plaintext.replace('a', '0')
    plaintext = plaintext.replace('b', '1')
    bin_list = []
    for i in range(0, len(plaintext), 5):
        bin_letter = plaintext[i:i + 5]
        bin_list.append(bin_letter)

    plaintext = ' '
    for item in bin_list:
        plaintext += chr(int(item, 2) + 97)
    return plaintext


def hash_based_on_input(func, input):
    if func == 'sha-256':
        val = hashlib.sha256(input.encode('utf-8'))
    elif func == 'sha-1':
        val = hashlib.sha1(input.encode('utf-8'))
    elif func == 'md5':
        val = hashlib.md5(input.encode('utf-8'))
    elif func == 'sha-384':
        val = hashlib.sha384(input.encode('utf-8'))
    elif func == 'sha-512':
        val = hashlib.sha512(input.encode('utf-8'))
    return val.hexdigest()


def hmac_based_on_input(func, input, key):
    if func == 'sha-256':
        val = hmac_import.new(key.encode('utf-8'), input.encode('utf-8'), hashlib.sha256)
    elif func == 'sha-1':
        val = hmac_import.new(key.encode('utf-8'), input.encode('utf-8'), hashlib.sha1)
    elif func == 'md5':
        val = hmac_import.new(key.encode('utf-8'), input.encode('utf-8'), hashlib.md5)
    elif func == 'sha-384':
        val = hmac_import.new(key.encode('utf-8'), input.encode('utf-8'), hashlib.sha384)
    elif func == 'sha-512':
        val = hmac_import.new(key.encode('utf-8'), input.encode('utf-8'), hashlib.sha512)
    return val.hexdigest()


def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.lower()
    key = key.lower()

    # Make key same amount of characters with plaintext
    while (len(plaintext) - len(key)) > len(key):
        key += key
    for i in range(0, len(plaintext) - len(key)):
        key += key[i]

    plaintext_int = [ord(i) for i in plaintext]
    key_int = [ord(i) for i in key]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        ciphertext += chr(((plaintext_int[i] - 97) + (key_int[i] - 97)) + 97)
    return ciphertext


def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.lower()
    key = key.lower()

    # Make key same amount of characters with plaintext
    while (len(ciphertext) - len(key)) > len(key):
        key += key
    for i in range(0, len(ciphertext) - len(key)):
        key += key[i]

    ciphertext_int = [ord(i) for i in ciphertext]
    key_int = [ord(i) for i in key]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        plaintext += chr(((ciphertext_int[i] - 97) - (key_int[i] - 97)) + 97)
    return plaintext


def a1z26_encrypt(plaintext):
    ciphertext = ""
    plaintext = plaintext.lower()  # Format to Lowercase
    plaintext = "".join(plaintext.split())  # Remove spaces from string
    for i in range(0, len(plaintext)):  # Loop through each character of string
        char = ord(plaintext[i]) - 96  # Convert character to numeric 1 - 26
        if 0 < char <= 26: ciphertext += str(char) + " "  # Store value in 'string' variable
    return ciphertext  # Return cipher string


def a1z26_decrypt(ciphertext):
    # Decrypt string by converting each number to a letter
    plaintext = ""  # Placeholder variable
    data = ciphertext.split()  # Split string at " "
    for char in data:  # Loop through each character
        char = chr(int(char) + 96)  # Convert number to letter
        plaintext += char  # Add character to string
    return plaintext  # Return plain string


def caesar_cipher_encrypt(plaintext, shift):
    final = []
    # transverse the plain text after accounting for spaces
    for word in plaintext.split():
        result = ""
        for i in range(len(word)):
            char = word[i]
            # Encrypt uppercase characters in plain text
            if word[i] in '!@#$%^&*()_+|\][}{\'":;/?.>,<1234567890':
                result += word[i]
            else:
                if char.isupper():
                    result += chr((ord(char) + shift - 65) % 26 + 65)
                # Encrypt lowercase characters in plain text
                else:
                    result += chr((ord(char) + shift - 97) % 26 + 97)
        final.append(result)

    return ' '.join(final)


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


def build_polybius_square(key=None, alphabet=None):
    if alphabet is None:
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # I and J are the same for polybius square
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
                    table[x][y] = key[x * 5 + y]
                    alphabet_list.remove(key[x * 5 + y])
                except IndexError:
                    table[x][y] = 0

        for x in range(5):
            for y in range(5):
                if table[x][y] == 0:
                    table[x][y] = alphabet_list[0]
                    del alphabet_list[0]

        return table


# TODO: Maybe this needs optimization, need to rethink
def bifid_encrypt_message(table, words):
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


# TODO: Maybe this needs optimization, need to rethink
def bifid_decrypt_message(table, words):
    ciphertext = [[0] * len(words) for row in range(2)]
    array = []
    words = words.upper()

    for index in range(len(words)):
        for row in range(len(table)):

            if words[index] in table[row]:
                array.append(row)
                array.append(table[row].index(words[index]))

    ciphertext[0] = array[:len(array) // 2]
    ciphertext[1] = array[len(array) // 2:]

    new_text = ''
    for index in range(len(words)):
        new_text += table[ciphertext[0][index]][ciphertext[1][index]]

    return new_text
