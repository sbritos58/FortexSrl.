from django.db import models
from django.contrib.auth.models import AbstractUser
from simple_history.models import HistoricalRecords


class Usuarios(AbstractUser):

	telefono = models.CharField(max_length=20,verbose_name='Teléfono',blank=False)
	history = HistoricalRecords()