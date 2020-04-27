from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .filters import OrdenesFilter
from .models import Clientes
from Register.models import Usuarios
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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
from django.db.models.functions import Lower


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

def ListClientesView(request):
	Model_one = Clientes.objects.all().order_by(Lower('rut'))

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
	return render(request, 'clientes/listClientes.html', context)


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