import django_filters
from django_filters import DateFilter

from .models import *

class OrdenesFilter(django_filters.FilterSet):
    class Meta:
        model = Stock
        fields = '__all__'

class StockMovimientosFilter(django_filters.FilterSet):
    fechaInicial = DateFilter(field_name="fecha" , lookup_expr='gte')
    fechaFinal = DateFilter(field_name="fecha" , lookup_expr='lte')
    class Meta:
        model = StockMovimientos
        fields = '__all__'