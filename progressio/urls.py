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
    path('stringuppercase', StringTransforms.stringuppercase, name='stringuppercase'),
    path('stringlowercase', StringTransforms.stringlowercase, name='stringlowercase'),
    path('stringlength', StringTransforms.stringlength, name='stringlength'),
    path('stringreverse', StringTransforms.stringreverse, name='stringreverse'),
    path('substringoccurence', StringTransforms.substringoccurrence, name='substringoccurence'),
    path('wordcounter', StringTransforms.wordcounter, name='wordcounter'),
    path('hextorgb', EncodingDecoding.hextorgb, name='hextorgb'),
    path('rgbtohex', EncodingDecoding.rgbtohex, name='rgbtohex'),
    path('base64encode', EncodingDecoding.base64encode, name='base64encode'),
    path('base64decode', EncodingDecoding.base64decode, name='base64decode'),
    path('base32encode', EncodingDecoding.base32encode, name='base32encode'),
    path('base32decode', EncodingDecoding.base32decode, name='base32decode'),
    path('stringtohex', EncodingDecoding.stringtohex, name='stringtohex'),
    path('hextostring', EncodingDecoding.hextostring, name='hextostring'),
    path('stringtobinary', EncodingDecoding.stringtobinary, name='stringtobinary'),
    path('binarytostring', EncodingDecoding.binarytostring, name='binarytostring'),
    path('htmlencode', EncodingDecoding.htmlencode, name='htmlencode'),
    path('htmldecode', EncodingDecoding.htmldecode, name='htmldecode'),
    path('urlencode', EncodingDecoding.urlencode, name='urlencode'),
    path('urldecode', EncodingDecoding.urldecode, name='urldecode'),
    path('decimaltobinary', EncodingDecoding.decimaltobinary, name='decimaltobinary'),
    path('binarytodecimal', EncodingDecoding.binarytodecimal, name='binarytodecimal'),
    path('decimaltohex', EncodingDecoding.decimaltohex, name='decimaltohex'),
    path('hextodecimal', EncodingDecoding.hextodecimal, name='hextodecimal'),
    path('caesarcipher', Cryptography.caesarcipher, name='caesarcipher'),
    path('enigmamachine', Cryptography.enigmamachine, name='enigmamachine'),
    path('affinecipherencrypt', Cryptography.affinecipherencrypt, name='affinecipherencrypt'),
    path('affinecipherdecrypt', Cryptography.affinecipherdecrypt, name='affinecipherdecrypt'),
    path('bifidencrypt', Cryptography.bifidencrypt, name='bifidencrypt'),
    path('bifiddecrypt', Cryptography.bifiddecrypt, name='bifiddecrypt'),
    path('rot13cipher', Cryptography.rot13cipher, name='rot13cipher'),
    path('a1z26cipherencrypt', Cryptography.a1z26cipherencrypt, name='a1z26cipherencrypt'),
    path('a1z26cipherdecrypt', Cryptography.a1z26cipherdecrypt, name='a1z26cipherdecrypt'),
    path('vigenerecipherencrypt', Cryptography.vigenerecipherencrypt, name='vigenerecipherencrypt'),
    path('vigenerecipherdecrypt', Cryptography.vigenerecipherdecrypt, name='vigenerecipherdecrypt'),
    path('baconcipherencrypt', Cryptography.baconcipherencrypt, name='baconcipherencrypt'),
    path('baconcipherdecrypt', Cryptography.baconcipherdecrypt, name='baconcipherdecrypt'),
    path('hashfunction', Cryptography.hashfunction, name='hashfunction'),
    path('hmac', Cryptography.hmac, name='hmac'),
    path('tapcodeencrypt', Cryptography.tapcodeencrypt, name='tapcodeencrypt'),
    path('tapcodedecrypt', Cryptography.tapcodedecrypt, name='tapcodedecrypt'),
    path('nihilistencrypt', Cryptography.nihilistencrypt, name='nihilistencrypt'),
    path('nihilistdecrypt', Cryptography.nihilistdecrypt, name='nihilistdecrypt'),
    path('trifidencrypt', Cryptography.trifidencrypt, name='trifidencrypt'),
    path('trifiddecrypt', Cryptography.trifiddecrypt, name='trifiddecrypt'),
    path('rc4encrypt', Cryptography.rc4encrypt, name='rc4encrypt'),
    path('rc4decrypt', Cryptography.rc4decrypt, name='rc4decrypt'),
    path('aesencrypt', Cryptography.aesencrypt, name='aesencrypt'),
    path('aesdecrypt', Cryptography.aesdecrypt, name='aesdecrypt')
]
