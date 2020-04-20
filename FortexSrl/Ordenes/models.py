from django.db import models
from Register.models import Usuarios
from Productos.models import Productos
from simple_history.models import HistoricalRecords


# Create your models here.
class Ordenes(models.Model):
    ESTADOS = (
        ('Ricevuto', 'Ricevuto'),
        ('Creato','Creato'),
        ('Assegnato','Assegnato'),
        ('Completato','Completato'),
        ('Consegnato','Consegnato'),
        ('Spedito', 'Spedito'),
        ('Inviato', 'Inviato'),
    )
    UBICACIONES = (
        ('Segretaria', 'Segretaria'),
        ('Fortex Nuova', 'Fortex Nuova'),
        ('Fortex Vecchia', 'Fortex Vecchia'),
        ('Cliente', 'Cliente'),
        ('Verniciatura', 'Verniciatura'),
        ('Controlo Qualità', 'Controlo Qualità'),
        ('Montaggio', 'Montaggio'),
        ('Graphic Design', 'Graphic Design'),

    )
    
    orden = models.AutoField(primary_key=True , blank=False,verbose_name='Número de órden')
    descripcion = models.TextField()
    producto = models.ForeignKey(Productos,verbose_name=('Prodotto'),on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20,choices=ESTADOS)
    cantidad_recibida = models.PositiveIntegerField(blank=False,null=True)
    ubicacion = models.CharField(max_length=20,choices=UBICACIONES)
    fecha_entrega_estimada=models.DateField(blank=True,null=True)
    asignado = models.ForeignKey(Usuarios, verbose_name=("Aseggnato a "),related_name='Asignado', on_delete=models.CASCADE)
    fecha_entrega_real = models.DateField(blank=True,null=True)
    usuarios = models.ForeignKey(Usuarios, verbose_name=("Creato"),on_delete=models.CASCADE, null=True,blank=False)
    cantidadEntregada = models.IntegerField(blank=True,null=True)
    telaio = models.IntegerField(blank=True,null=True)
    history = HistoricalRecords()
    
    def __str__(self):
        return str(self.orden)

