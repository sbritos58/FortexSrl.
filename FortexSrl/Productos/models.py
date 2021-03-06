from django.db import models
from Clientes.models import Clientes
from simple_history.models import HistoricalRecords
from Register.models import Usuarios
from Stock.models import Stock

# Create your models here.


class Productos(models.Model):

    nombre = models.CharField(blank=False, max_length=50)
    rut = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    material = models.CharField(blank=True, max_length=50)
    plasma = models.CharField(blank=True, max_length=50)
    preTratamiento = models.ManyToManyField(Stock,related_name='+',blank=True)
    fondo = models.ManyToManyField(Stock,related_name="+",blank=True)
    finitura = models.ManyToManyField(Stock,blank=True)
    deposito = models.CharField(blank=True, max_length=150)
    controlCalidad = models.CharField(blank=True, max_length=50)
    embalaje = models.CharField(blank=True, max_length=50)
    consideraciones = models.TextField(blank=True)
    temperatura = models.IntegerField(blank=True,null=True)
    tiempo_horno = models.IntegerField(blank=True,null=True)
    fotos = models.ImageField(blank=True)
    telaio = models.PositiveSmallIntegerField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,blank=True)
    usuarios = models.ForeignKey(Usuarios, verbose_name=("Creado por "), on_delete=models.CASCADE)
    history = HistoricalRecords()
    
    def __str__(self):
        return self.nombre