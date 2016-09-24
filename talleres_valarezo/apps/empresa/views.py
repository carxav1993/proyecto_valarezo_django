from django.shortcuts import render
from .models import Empresa, Servicio, Contacto
# Create your views here.

def index (request):
	empresa = Empresa.objects.get(pk=2)
	return render(request, 'empresa/index.html', {'empresa':empresa})

def nosotros(request):
	empresa = Empresa.objects.all()[1]
	return render(request, 'empresa/nosotros.html',{'empresa':empresa})

def servicios(request):
	return render(request, 'empresa/servicios.html')

def contactenos(request):
	return render(request, 'empresa/contactenos.html')