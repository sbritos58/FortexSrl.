from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Clientes
from Register.models import Usuarios


from django.views.generic import DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import ClientesForm
from django.contrib.auth import get_user_model

class CreateClientesView(SuccessMessageMixin, CreateView):

	form_class = ClientesForm
	template_name = 'clientes/create.html'


	def form_valid(self,form):
		formulario = form.save(commit=False)
		formulario.usuarios =self.request.user
		updated_event = formulario.save()
		messages.success(self.request, '¡¡¡ Cliente %s Creado correctamente !!!' % (formulario.nombre_organizacion))
		return super().form_valid(form)


	def get_success_url(self):
		return reverse_lazy('ListClientes')

class UpdateClientesView(SuccessMessageMixin,UpdateView):
	form_class = ClientesForm
	model = Clientes
	template_name = 'clientes/update.html'

	def form_valid(self,form):
		formulario = form.save(commit=False)
		updated_event = formulario.save()
		messages.success(self.request, '¡¡¡ Cliente %s modificado correctamente !!!' % (formulario.nombre_organizacion))
		return super().form_valid(form)

	def get_success_url(self):
		return reverse_lazy('ListClientes')

class ListClientesView(ListView):
	form_class = ClientesForm
	model = Clientes
	template_name = 'clientes/listClientes.html'
	paginate_by = 3

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(ListClientesView, self).get_context_data(**kwargs)
		context["total"] = Clientes.objects.all().count
		return context

class DeleteClientesView(DeleteView):
	form_class = ClientesForm
	model = Clientes
	def get_success_url(self):
		success_message = '¡¡¡ Cliente eliminado correctamente !!!'
		messages.success(self.request,(success_message))
		return reverse_lazy('ListClientes')

class DetailClientesView(DetailView):
	form_class = ClientesForm
	model = Clientes
	template_name = 'clientes/detail.html'