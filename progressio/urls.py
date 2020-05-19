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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StringTransforms.index, name='index'),
    path('stringlength', StringTransforms.stringLength, name='stringlength'),
    path('stringreverse', StringTransforms.stringReverse, name='stringreverse'),
    path('base64encode', EncodingDecoding.base64encode, name='base64encode'),
    path('base64decode', EncodingDecoding.base64decode, name='base64decode'),
    path('base32encode', EncodingDecoding.base32encode, name='base32encode'),
    path('base32decode', EncodingDecoding.base32decode, name='base32decode')
]
