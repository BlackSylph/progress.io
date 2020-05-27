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

handler404 = Globals.handler404
handler500 = Globals.handler500

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
    path('htmlencode', EncodingDecoding.html_encode, name='htmlencode'),
    path('htmldecode', EncodingDecoding.html_decode, name='htmldecode'),
    path('urlencode', EncodingDecoding.url_encode, name='urlencode'),
    path('urldecode', EncodingDecoding.url_decode, name='urldecode'),
    # CIPHER FUNCTIONS START HERE
    path('caesarcipher', Cryptography.caesarcipher, name='caesarcipher'),
    path('enigmamachine', Cryptography.enigmamachine, name='enigmamachine'),
    path('affinecipher', Cryptography.affinecipher, name='affinecipher'),
    path('bifidcipher', Cryptography.bifidcipher, name='bifidcipher'),
    path('rot13cipher', Cryptography.rot13cipher, name='rot13cipher'),
    path('a1z26cipher', Cryptography.a1z26cipher, name='a1z26cipher'),
    path('vigenerecipher', Cryptography.vigenerecipher, name='vigenerecipher'),
    path('baconcipher', Cryptography.baconcipher, name='baconcipher'),
    path('hashfunction', Cryptography.hashfunction, name='hashfunction'),
    path('hmac', Cryptography.hmac, name='hmac'),
    path('tapcodecipher', Cryptography.tapcodecipher, name='tapcodecipher'),
    path('nihilistcipher', Cryptography.nihilistcipher, name='nihilistcipher'),
    path('trifid', Cryptography.trifidcipher, name='trifid'),
    path('rc4', Cryptography.rc4cipher, name='rc4'),
    path('aes', Cryptography.aes, name='aes')
]
