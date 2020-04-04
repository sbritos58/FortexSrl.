from django.shortcuts import render
from .models import Ordenes
from .forms import OrdenesForm,HistoryForm

from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from datetime import date
# Create your views here.
class CreateOrdenView(SuccessMessageMixin,CreateView):
    form_class = OrdenesForm
    template_name = 'ordenes/createOrden.html'

    def get_success_url(self):
        return reverse_lazy('listarOrden')

    def form_valid(self, form):
        formulario = form.save(commit=False)

        if formulario.estado == 'Entregado' and formulario.ubicacion == 'Cliente':
            formulario.fecha_entrega_real = date.today()
        else:
            formulario.fecha_entrega_real = None
        formulario.usuarios = self.request.user
        updated_event = formulario.save()
        messages.success(self.request,'¡¡¡ Orden %s creada correctamente !!!' %(formulario.orden))
        return super().form_valid(form)

class ListOrdenView(ListView):
    model = Ordenes
    form_class = OrdenesForm
    second_form_class = HistoryForm
    template_name = 'ordenes/listOrden.html'

    def get_context_data(self, **kwargs):
        context = super(ListOrdenView,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = Ordenes.objects.all()
        if 'form2' not in context:
            context['form2'] = Ordenes.history.all().order_by('orden')
        return context


class DetailOrdenView(DetailView):
    form_class = OrdenesForm
    model = Ordenes
    template_name = 'ordenes/detailOrden.html'

class DeleteOrdenView(DeleteView):
    model = Ordenes

    def get_success_url(self):
        success_message = '¡¡¡ Producto eliminado correctamente !!!'
        messages.success(self.request, (success_message))
        return reverse_lazy('listarOrden')

class UpdateOrdenView(UpdateView):
    form_class = OrdenesForm
    model = Ordenes
    template_name = 'ordenes/updateOrden.html'

    def get_success_url(self):
        return reverse_lazy('listarOrden')

    def form_valid(self, form):
        formulario = form.save(commit=False)

        if formulario.estado == 'Entregado' and formulario.ubicacion == 'Cliente':
            formulario.fecha_entrega_real = date.today()
        else:
            formulario.fecha_entrega_real = None
        formulario.usuarios = self.request.user
        updated_event = formulario.save()
        messages.success(self.request, '¡¡¡ La orden %s se ha modificado correctamente !!!' % (formulario.orden))
        return super().form_valid(form)

