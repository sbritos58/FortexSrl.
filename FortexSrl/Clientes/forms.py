from django import forms
from .models import Clientes

class ClientesForm(forms.ModelForm):
	class Meta:
		model = Clientes
		fields = ['rut','nombre_organizacion','nombre','apellido','direccion1','direccion2','ciudad','telefono','celular','email','tipo_cliente']
		