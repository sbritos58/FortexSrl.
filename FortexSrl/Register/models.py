from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuarios(AbstractUser):

	telefono = models.CharField(max_length=20,null=True, verbose_name='Teléfono',blank=False)

	class Meta:
		permissions = (('Administrador', 'Administrador'),
					   ('Encargado','Encargado'),
					   ('Pintor','Pintor'),
					   ('Montaje','Montaje'),
					   ('Calidad1','Calidad1'),
					   ('Secretaria','Secretaria'),
					   ('Stock','Stock'),
					   )