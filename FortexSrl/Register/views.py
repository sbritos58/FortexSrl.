from django.shortcuts import render
from .models import Usuarios
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView


# Create your views here.


class CreateUserView(SuccessMessageMixin, CreateView):
    model = Usuarios
    template_name = 'register/Registro.html'
    fields = ['username', 'first_name', 'last_name', 'telefono', 'email', 'is_active', 'is_staff', 'groups', 'password']
    success_message = 'Usuario creado correctamente!'

    def get_success_url(self):
        return reverse_lazy('listViewUsuario')


class UpdateUserView(SuccessMessageMixin, UpdateView):
    model = Usuarios
    template_name = 'register/update.html'
    fields = ['username', 'first_name', 'last_name', 'telefono', 'email', 'is_active', 'is_staff', 'groups']
    success_message = 'Usuario modificado correctamente!'

    def get_success_url(self):
        return reverse_lazy('listViewUsuario')


class ListUserView(ListView):
    model = Usuarios
    ordering = '-first_name'
    template_name = 'register/ListView.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListUserView, self).get_context_data(**kwargs)
        context["total"] = Usuarios.objects.all().count
        return context


class DetailUserView(DetailView):
    model = Usuarios
    template_name = 'register/detail.html'


class DeleteUserView(DeleteView):
    model = Usuarios

    def get_success_url(self):
        success_message = '¡¡¡ Usuario eliminado correctamente !!!'
        messages.success(self.request, (success_message))
        return reverse_lazy('listViewUsuario')
