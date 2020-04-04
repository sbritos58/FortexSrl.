from django.db import models
from Register.models import Usuarios
from Productos.models import Productos
from simple_history.models import HistoricalRecords


# Create your models here.
class Ordenes(models.Model):
    ESTADOS = (
        ('Recibido', 'Recibido'),
        ('Creado','Creado'),
        ('Asignado','Asignado'),
        ('Finalizado','Finalizado'),
        ('Entregado','Entregado'),
        ('Despachado', 'Despachado'),
        ('Enviado', 'Enviado'),
    )
    UBICACIONES = (
        ('Secretaria', 'Secretaria'),
        ('Fortex Nueva', 'Fortex Nueva'),
        ('Fortex Vieja', 'Fortex Vieja'),
        ('Cliente', 'Cliente'),
        ('Verniciatura', 'Verniciatura'),
        ('Control Calidad', 'Control Calidad'),
        ('Montaje', 'Montaje'),
        ('Diseño gráfico', 'Diseño gráfico'),
    )
    
    orden = models.AutoField(primary_key=True , blank=False,verbose_name='Número de órden')
    descripcion = models.TextField()
    producto = models.ForeignKey(Productos,verbose_name=('Producto'),on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20,choices=ESTADOS)
    cantidad = models.PositiveIntegerField(blank=False)
    ubicacion = models.CharField(max_length=20,choices=UBICACIONES)
    fecha_entrega_estimada=models.DateField(blank=True,null=True)
    asignado = models.ForeignKey(Usuarios, verbose_name=("Asignado a "),related_name='Asignado', on_delete=models.CASCADE)
    fecha_entrega_real = models.DateField(blank=True,null=True)
    usuarios = models.ForeignKey(Usuarios, verbose_name=("Creado por "),on_delete=models.CASCADE, null=True,blank=False)
    history = HistoricalRecords()
    
    def __str__(self):
        return str(self.orden)

