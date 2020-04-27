from django.db import models
# Create your models here.

class Stock(models.Model):
    TIPO_PRODUCTO = (
        ('Fondo','Fondo'),
        ('Finitura','Finitura'),
        ('Pre_tratamiento','Pre_tratamiento'),
    )

    nombre = models.CharField(max_length=100,null=False,blank=False)
    descripcion = models.TextField(blank=True,null=True)
    cantidad = models.PositiveIntegerField(blank=False,null=False)
    tipo_de_producto = models.CharField(choices=TIPO_PRODUCTO,max_length=15,blank=True,null=True)
    proveedor = models.CharField(max_length=50,null=False,blank=False)
    precio = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.nombre

class StockMovimientos(models.Model):


    nombre = models.ForeignKey(Stock,on_delete=models.CASCADE,blank=False,null=False)
    tipo_de_movimiento = models.BooleanField(blank=False,null=False)
    cantidad =models.FloatField(blank=False,null=False)
    orden = models.ForeignKey("Ordenes.Ordenes",on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True,blank=False,null=False)
    
    def __str__(self):
        if tipo_de_movimiento == True:
            return self.nombre + " Suma"
        elif tipo_de_movimiento == False:
            return self.nombre + " Resta"