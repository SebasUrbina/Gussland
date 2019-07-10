from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categoria(models.Model):
	nombre=models.CharField(max_length=20)
	def __str__(self):
		return self.nombre
class Producto(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=512)
	precio=models.IntegerField(max_length=50)
	categoria=models.ForeignKey(Categoria,null=True,on_delete=models.CASCADE)

class Cliente(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	nombre=models.CharField(max_length=30)
	apellido=models.CharField(max_length=30)
	telefono=models.IntegerField(max_length=9)
	correo=models.EmailField(max_length=256)
	direccion=models.CharField(max_length=256)

class Pedido(models.Model): 
	producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
	cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
	fecha=models.DateTimeField()	
	comentario=models.TextField(max_length=512)
	listo=models.BooleanField(default=False)

	def display_pedido(self):
		return self.producto.nombre
	def display_cliente(self):
		return self.cliente.nombre

class Promocion(models.Model): 
	nombre=models.CharField(max_length=30) 
	valor=models.IntegerField()

class Promoproducto(models.Model):
	producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
	promocion=models.ForeignKey(Promocion,on_delete=models.CASCADE)	

	def display_producto(self):
		return self.producto.nombre
	def display_promo(self):
		return self.promocion.nombre