from django import forms
from .models import Usuarios
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UsuariosForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Usuarios
        fields = ['username', 'first_name', 'last_name', 'telefono', 'email', 'is_active', 'is_staff', 'groups', 'password1', 'password2']

        # def clean_password1(self):
        #     password1 = self.cleaned_data(password1)
        #     return password1
        #
        # def clean_password2(self):
        #     password2 = self.cleaned_data(password2)
        #     return password2

    def save(self, commit=True):
        try:
            user = super().save(commit=False)
            user.set_password(self.cleaned_data['password1'])
            user.save()
            user.groups.clear()
            groups = self.cleaned_data['groups']
            for i in groups:
                user.groups.add(i)
        except Exception as e:
            print(e)
