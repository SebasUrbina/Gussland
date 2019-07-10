from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
	path('',views.index,name='index'),
	path('contacto',views.contacto,name='contacto'),
	path('nosotros',views.nosotros,name='nosotros'),
	path('carta',views.carta,name='carta'),
	]