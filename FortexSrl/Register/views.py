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
from .filters import OrdenesFilter
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import UsuariosForm


# Create your views here.


class CreateUserView(SuccessMessageMixin, CreateView):
    form_class = UsuariosForm
    template_name = 'register/Registro.html'
    success_message = '¡¡ Utente creato con successo !!'

    def form_valid(self, form):
        print(form)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form)
        return super().form_invalid(form)

    # def form_valid(self, form):
    #     form = super(CreateUserView, self).form_valid(form)
    #
    #     return form
    #
    # def form_invalid(self, form):
    #     form = super(CreateUserView, self).form_invalid(form)
    #     print("algo no funciono")
    #     return form

    def get_success_url(self):
        return reverse_lazy('listViewUsuario')


class UpdateUserView(SuccessMessageMixin, UpdateView):
    model = Usuarios
    template_name = 'register/update.html'
    fields = ['username', 'first_name', 'last_name', 'telefono', 'email', 'is_active', 'is_staff', 'groups']
    success_message = '¡¡ Utente modificato con successo !'

    def get_success_url(self):
        return reverse_lazy('listViewUsuario')


def ListUserView(request):
    Model_one = Usuarios.objects.all()

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
    return render(request, 'register/listView.html', context)


class DetailUserView(DetailView):
    model = Usuarios
    template_name = 'register/detail.html'


class DeleteUserView(DeleteView):
    model = Usuarios

    def get_success_url(self):
        success_message = '¡¡ Utente cancelatto con successo !!'
        messages.success(self.request, (success_message))
        return reverse_lazy('listViewUsuario')
