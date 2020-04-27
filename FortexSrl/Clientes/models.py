from django.db import models
from Register.models import Usuarios
from simple_history.models import HistoricalRecords
from django.conf import settings
# Create your models here.

class Clientes(models.Model):
	TIPO_CLIENTE = (
		('Oro','Oro'),
		('Plata','Plata'),
		('Bronce','Bronce'),
		)
	rut = models.IntegerField(primary_key=True,blank=False,null=False)
	nombre_organizacion = models.CharField(max_length=50,blank=False,null=False)
	nombre = models.CharField(max_length=50, blank=False,null=False)
	apellido = models.CharField(max_length=50,blank=False,null=False)
	direccion1 = models.CharField(max_length=150,blank=True,null=False)
	direccion2 = models.CharField(max_length=150, blank=True,null=False)
	ciudad = models.CharField(max_length=20,blank=True,null=False)
	telefono = models.CharField(max_length=20,blank=True,null=False)
	celular = models.CharField(max_length=20,blank=True,null=False)
	email = models.EmailField(max_length=254, blank=True,null=False)
	tipo_cliente = models.CharField(max_length=10,choices=TIPO_CLIENTE,null=False)
	usuarios = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, verbose_name=("Creado por "),on_delete=models.CASCADE)
	history = HistoricalRecords()

	def __str__(self):
		return self.nombre_organizacion