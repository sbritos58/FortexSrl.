import django_filters
from django_filters import CharFilter
from .models import *

class OrdenesFilter(django_filters.FilterSet):
    nombre_organizacion = CharFilter(field_name="nombre_organizacion",lookup_expr="icontains")
    nombre = CharFilter(field_name="nombre", lookup_expr="icontains")
    apellido = CharFilter(field_name="apellido", lookup_expr="icontains")
    email = CharFilter(field_name="email", lookup_expr="icontains")

    class Meta:
        model = Clientes
        fields = '__all__'
        exclude = 'fotos'

class HistoryFilter(django_filters.FilterSet):

    class Meta:
        models = Clientes
        fields = 'history'
