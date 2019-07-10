from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'gus_app/index.html')

def contacto(request):
	return render(request,'gus_app/contacto.html')

def nosotros(request):
	return render(request,'gus_app/nosotros.html')

def carta(request):
	return render(request,'gus_app/carta.html')
