from django import forms
from .models import Productos


class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre','rut','material','preTratamiento','plasma','fondo','deposito','finitura','controlCalidad','embalaje','consideraciones','fotos','telaio']