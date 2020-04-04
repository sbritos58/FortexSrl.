from django import forms
from .models import Ordenes

class OrdenesForm(forms.ModelForm):
    class Meta:
        model = Ordenes
        fields = ['descripcion','producto','estado','ubicacion','fecha_entrega_estimada','asignado']

class HistoryForm(forms.ModelForm):
    class Meta:
        model = Ordenes
        fields = '__all__'