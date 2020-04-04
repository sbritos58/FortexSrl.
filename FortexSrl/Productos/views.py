from Register.models import Usuarios
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from .forms import ProductosForm
from .models import Productos

#TODO: hacer en cada template el poder registrar un tipo de campo que no exista en los foreignkey

class CreateProductosView(SuccessMessageMixin,CreateView):
    form_class = ProductosForm
    template_name = 'productos/create.html'

    def get_success_url(self):
        return reverse_lazy('listProductos')

    def form_valid(self, form):
        formulario = form.save(commit=False)
        formulario.usuarios = self.request.user
        updated_event = formulario.save()
        messages.success(self.request,'¡¡¡ Producto %s Creado correctamente !!!' %(formulario.nombre))
        return super().form_valid(form)



class ListProductosView(ListView):
    model = Productos
    form_class = ProductosForm
    template_name = 'productos/listProductos.html'

class UpdateProductosView(SuccessMessageMixin,UpdateView):
    form_class = ProductosForm
    model = Productos
    template_name = 'Productos/updateProductos.html'

    def get_success_url(self):
        return reverse_lazy('listProductos')


    def form_valid(self, form):
        formulario = form.save(commit=False)
        messages.success(self.request,'¡¡¡ Producto %s modificado correctamente !!!' %(formulario.nombre))
        return super().form_valid(form)

class DeleteProductosView(DeleteView):
    model = Productos

    def get_success_url(self):

        success_message = '¡¡¡ Producto eliminado correctamente !!!'
        messages.success(self.request,(success_message))
        return reverse_lazy('listProductos')

class DetailProductosView(DetailView):
    form_class = ProductosForm
    model = Productos
    template_name = 'Productos/detailProductos.html'