"""progressio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .Views.Globals import views as Globals
from .Views.StringTransforms import views as StringTransforms
from .Views.EncodingDecoding import views as EncodingDecoding
from .Views.Cryptography import views as Cryptography

handler404 = Globals.handler_404
handler500 = Globals.handler_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StringTransforms.index, name='index'),
    # STRING FUNCTIONS START HERE
    path('stringbasicmanipulation', StringTransforms.string_basic_manipulation, name='stringbasicmanipulation'),
    path('stringlength', StringTransforms.string_length, name='stringlength'),
    path('substringoccurrence', StringTransforms.substring_occurrence, name='substringoccurrence'),
    path('wordcounter', StringTransforms.word_counter, name='wordcounter'),
    # ENCODE/DECODE FUNCTIONS START HERE
    path('hextorgb', EncodingDecoding.hex_to_rgb, name='hextorgb'),
    path('rgbtohex', EncodingDecoding.rgb_to_hex, name='rgbtohex'),
    path('base64', EncodingDecoding.base_64, name='base64'),
    path('base32', EncodingDecoding.base_32, name='base32'),
    path('stringtobinary', EncodingDecoding.string_to_binary, name='stringtobinary'),
    path('binarytostring', EncodingDecoding.binary_to_string, name='binarytostring'),
    path('stringtohex', EncodingDecoding.string_to_hex, name='stringtohex'),
    path('hextostring', EncodingDecoding.hex_to_string, name='hextostring'),
    path('decimaltobinary', EncodingDecoding.decimal_to_binary, name='decimaltobinary'),
    path('binarytodecimal', EncodingDecoding.binary_to_decimal, name='binarytodecimal'),
    path('decimaltohex', EncodingDecoding.decimal_to_hex, name='decimaltohex'),
    path('hextodecimal', EncodingDecoding.hex_to_decimal, name='hextodecimal'),
    path('htmlencodedecode', EncodingDecoding.html_encode_decode, name='htmlencodedecode'),
    path('urlencodedecode', EncodingDecoding.url_encode_decode, name='urlencodedecode'),
    # CIPHER FUNCTIONS START HERE
    path('caesarcipher', Cryptography.caesar_cipher, name='caesarcipher'),
    path('enigmamachine', Cryptography.enigma_machine, name='enigmamachine'),
    path('affinecipher', Cryptography.affine_cipher, name='affinecipher'),
    path('bifidcipher', Cryptography.bifid_cipher, name='bifidcipher'),
    path('rot13cipher', Cryptography.rot13_cipher, name='rot13cipher'),
    path('a1z26cipher', Cryptography.a1z26_cipher, name='a1z26cipher'),
    path('vigenerecipher', Cryptography.vigenere_cipher, name='vigenerecipher'),
    path('baconcipher', Cryptography.bacon_cipher, name='baconcipher'),
    path('hashfunction', Cryptography.hash_function, name='hashfunction'),
    path('hmac', Cryptography.hmac, name='hmac'),
    path('tapcodecipher', Cryptography.tap_code_cipher, name='tapcodecipher'),
    path('nihilistcipher', Cryptography.nihilist_cipher, name='nihilistcipher'),
    path('trifid', Cryptography.trifid_cipher, name='trifid'),
    path('rc4', Cryptography.rc4_cipher, name='rc4'),
    path('aes', Cryptography.aes, name='aes')
]
