from django import forms
from .models import Usuarios
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UsuariosForm(UserCreationForm):
   class Meta(UserCreationForm):
       model = Usuarios
       fields = ['username', 'first_name', 'last_name', 'telefono', 'email', 'is_active', 'is_staff', 'groups','password1','password2']

