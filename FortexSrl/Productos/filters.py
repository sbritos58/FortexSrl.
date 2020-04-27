import django_filters
from django_filters import CharFilter

from .models import *

class OrdenesFilter(django_filters.FilterSet):
    nombre = CharFilter(field_name="nombre" ,lookup_expr="icontains")
    material = CharFilter(field_name="material",lookup_expr="icontains")

    class Meta:
        model = Productos
        fields = '__all__'
        exclude = 'fotos'

class HistoryFilter(django_filters.FilterSet):

    class Meta:
        models = Productos
        fields = 'history'
