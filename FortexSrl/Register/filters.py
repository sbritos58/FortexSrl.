import django_filters

from .models import *

class OrdenesFilter(django_filters.FilterSet):
    class Meta:
        model = Usuarios
        fields = '__all__'