import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrdenesFilter(django_filters.FilterSet):
    nombre = CharFilter(field_name="nombre" ,lookup_expr="icontains")

    class Meta:
        model = Stock
        fields = '__all__'

class StockMovimientosFilter(django_filters.FilterSet):
    fechaInicial = DateFilter(field_name="fecha" , lookup_expr='gte')
    fechaFinal = DateFilter(field_name="fecha" , lookup_expr='lte')
    class Meta:
        model = StockMovimientos
        fields = '__all__'