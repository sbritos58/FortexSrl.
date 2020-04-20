from django import forms
from .models import Usuarios

class UsuariosForm(forms.Form):
   class Meta:
       model = Usuarios
       fields = ['username', 'first_name', 'last_name', 'telefono', 'email', 'is_active', 'is_staff', 'groups','password']


