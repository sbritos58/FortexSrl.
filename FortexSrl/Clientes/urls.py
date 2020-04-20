from django.urls import path,include
from .views import CreateClientesView,UpdateClientesView,ListClientesView,DeleteClientesView,DetailClientesView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('Clientes/crear/',login_required(CreateClientesView.as_view()),name='createClientes'),
    path('Clientes/update/<int:pk>',login_required(UpdateClientesView.as_view()),name='updateClientes'),
    path('Clientes',login_required(ListClientesView.as_view()),name='ListClientes'),
    path('Clientes/delete/<int:pk>',login_required(DeleteClientesView.as_view()),name='deleteClientes'),
    path('Clientes/detail/<int:pk>',login_required(DetailClientesView.as_view()),name='detailClientes'),
]