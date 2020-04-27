from django import forms
from .models import Productos
from Stock.models import Stock

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ('nombre','rut','material','preTratamiento','plasma','fondo','deposito','finitura','controlCalidad','embalaje','consideraciones','temperatura','tiempo_horno','fotos','fotos','telaio')

    nombre = forms.CharField()
    rut = forms.SelectMultiple()
    material = forms.CharField()
    preTratamiento = forms.ModelMultipleChoiceField(queryset=Stock.objects.filter(tipo_de_producto='Pre_tratamiento'))
    plasma = forms.CharField()
    fondo = forms.ModelMultipleChoiceField(queryset=Stock.objects.filter(tipo_de_producto="Fondo"))
    deposito = forms.Textarea()
    finitura = forms.ModelMultipleChoiceField(queryset=Stock.objects.filter(tipo_de_producto="Finitura"))
    controlCalidad = forms.Textarea()
    embalaje = forms.CharField()
    consideraciones = forms.Textarea()
    fotos = forms.ImageField(required=False)
    telaio = forms.IntegerField(required=False)

