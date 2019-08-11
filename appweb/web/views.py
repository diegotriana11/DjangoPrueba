from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from appweb.web.form_municipio import MunicipioForm
from appweb.web.form_regiones import RegionForm
from appweb.web.models import *


def index(request):
	return render(request, "index.html")

def home_view(*args,**kwargs):
	return HttpResponse("<h1>Welcome</h1>")

def municipio_view(request):
	if request.method == 'POST':
		form = MunicipioForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect(municipios_lista)
	else:
		form = MunicipioForm()

	return render(request, 'municipios_form.html', {'form':form })


def region_view(request):
	if request.method == 'POST':
		form = RegionForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect(regiones_lista)
	else:
		form = RegionForm()

	return render(request, 'regiones_form.html', {'form':form })

def municipios_lista(request):
	municipios = Municipio.objects.all().order_by('id')
	contexto = {'municipios':municipios}
	return render(request, 'municipios_lista.html',contexto)

def regiones_lista(request):
	regiones = Region.objects.all().order_by('id')
	contexto = {'regiones':regiones}
	return render(request, 'regiones_lista.html',contexto)

def municipio_edit(request, id_municipio):
	municipio = Municipio.objects.get(id=id_municipio)
	if request.method == 'GET':
		form = MunicipioForm(instance=municipio)
	else:
		form = MunicipioForm(request.POST, instance=municipio)
		if form.is_valid():
			form.save()
		return redirect(municipios_lista)
	return render(request,'municipios_form.html', {'form':form} )

def removeMunicipioFromRegion():
	return ""

def region_edit(request, id_region):
	region = Region.objects.get(id=id_region)
	if request.method == 'GET':
		form = RegionForm(instance=region)
	else:
		form = RegionForm(request.POST, instance=region)
		if form.is_valid():
			form.save()
		return redirect(regiones_lista)
	return render(request,'regiones_form.html', {'form':form} )

def municipio_delete(request, id_municipio):
	municipio = Municipio.objects.get(id=id_municipio)
	if request.method == 'POST':
		municipio.delete()
		return redirect(municipios_lista)
	return render(request,'municipio_delete.html', {'municipio':municipio} )

def region_delete(request, id_region):
	region = Region.objects.get(id=id_region)
	if request.method == 'POST':
		region.delete()
		return redirect(regiones_lista)
	return render(request,'region_delete.html', {'region':region} )