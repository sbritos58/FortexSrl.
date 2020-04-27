from Register.models import Usuarios
from django.shortcuts import render

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
from .filters import OrdenesFilter
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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



def ListProductosView(request):
    Model_one = Productos.objects.all()

    myFilter = OrdenesFilter(request.GET, queryset=Model_one)
    paginator = Paginator(myFilter.qs, 10)
    page = request.GET.get('page1')
    try:
        pub = paginator.page(page)
    except PageNotAnInteger:
        pub = paginator.page(1)
    except EmptyPage:
        pub = paginator.page(paginator.num_pages)

    myFilter = OrdenesFilter(request.GET, queryset=Model_one)

    context = {'Model_one': Model_one, 'pub': pub, "myFilter": myFilter}
    return render(request, 'productos/listProductos.html', context)

class UpdateProductosView(SuccessMessageMixin,UpdateView):
    form_class = ProductosForm
    model = Productos
    template_name = 'Productos/listProductos.html'

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