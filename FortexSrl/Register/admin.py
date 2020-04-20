from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuarios
from django.contrib.auth.forms import UserCreationForm





admin.site.register(Usuarios,UserAdmin)

# Register your models here.
