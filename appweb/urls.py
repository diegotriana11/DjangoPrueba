"""appweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from appweb.web.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo_municipio$', municipio_view),
    url(r'^nuevo_region$', region_view),
    url(r'^lista_municipios$',municipios_lista),
    url(r'^lista_regiones$',regiones_lista),
    url(r'^municipio_edit/(?P<id_municipio>\d+)/$',municipio_edit),
    url(r'^region_edit/(?P<id_region>\d+)/$',region_edit),
    url(r'^municipio_delete/(?P<id_municipio>\d+)/$',municipio_delete),
    url(r'^region_delete/(?P<id_region>\d+)/$',region_delete)
]


""" 
urlpatterns = [
    url('admin/', admin.site.urls),
    path('', index),
    path('nuevo_municipio', municipio_view),
    path('nuevo_region', region_view),
    path('lista_municipios', municipios_lista),
    path('lista_regiones', regiones_lista),
    path('municipio_edit/?')
]"""
 
 #path('admin/', admin.site.urls),