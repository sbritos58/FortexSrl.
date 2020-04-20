from django.db import models
# Create your models here.

class Stock(models.Model):
    TIPO_PRODUCTO = (
        ('Fondo','Fondo'),
        ('Finitura','Finitura'),
        ('Pre_tratamiento','Pre_tratamiento'),
    )
    UNIDADES = (
        (1,'Kgs.'),
        (2,'Grs.'),
        (3,'Ltrs.'),
        (4,'Mltrs.'),
    )
    nombre = models.CharField(max_length=100,null=False,blank=False)
    descripcion = models.TextField(blank=True,null=True)
    cantidad = models.PositiveIntegerField(blank=False,null=False)
    unidades = models.SmallIntegerField(choices=UNIDADES,blank=False,null=False)
    tipo_de_producto = models.CharField(choices=TIPO_PRODUCTO,max_length=15,blank=True,null=True)
    proveedor = models.CharField(max_length=50,null=False,blank=False)
    precio = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.nombre