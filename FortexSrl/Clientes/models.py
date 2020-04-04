from django.db import models
from Register.models import Usuarios
from simple_history.models import HistoricalRecords

# Create your models here.

class Clientes(models.Model):
	TIPO_CLIENTE = (
		('Oro','Oro'),
		('Plata','Plata'),
		('Bronce','Bronce'),
		)
	rut = models.IntegerField(primary_key=True,blank=False,unique=True)
	nombre_organizacion = models.CharField(max_length=50,blank=False)
	nombre = models.CharField(max_length=50, blank=False)
	apellido = models.CharField(max_length=50,blank=False)
	direccion1 = models.CharField(max_length=150,blank=True)
	direccion2 = models.CharField(max_length=150, blank=True)
	ciudad = models.CharField(max_length=20,blank=True)
	telefono = models.CharField(max_length=20,blank=True)
	celular = models.CharField(max_length=20,blank=True)
	email = models.EmailField(max_length=254, blank=True)
	tipo_cliente = models.CharField(max_length=10,choices=TIPO_CLIENTE)
	usuarios = models.ForeignKey("Register.Usuarios", verbose_name=("Creado por "),on_delete=models.CASCADE)
	history = HistoricalRecords()

	def __str__(self):
		return self.nombre_organizacion