import django_filters

from .models import *

class OrdenesFilter(django_filters.FilterSet):
    class Meta:
        model = Ordenes
        fields = ('orden','producto','estado','ubicacion','asignado','usuarios')

class HistoryFilter(django_filters.FilterSet):

    class Meta:
        models = Ordenes
        fields = 'history'
