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
from .Views.StringTransforms import views as StringTransforms
from .Views.EncodingDecoding import views as EncodingDecoding
from .Views.Globals import views as Globals
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
    path('affinecipherdecrypt', Cryptography.affinecipherdecrypt, name='affinecipherdecrypt')
]
