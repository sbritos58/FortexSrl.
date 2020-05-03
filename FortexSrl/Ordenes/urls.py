from django.urls import path,include
from .views import CreateOrdenView,ListViewOrden,DetailOrdenView,DeleteOrdenView,UpdateOrdenView,dashboard,ListHistorialView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('Ordenes/crear/',login_required(CreateOrdenView.as_view()),name='crearOrden'),
    path('Ordenes/list',login_required(ListViewOrden),name = 'listarOrden'),
    path('Ordenes/detail/<int:pk>',login_required(DetailOrdenView.as_view()), name = 'detailOrden'),
    path('',login_required(dashboard), name = 'dashboard'),

    path('Ordenes/history/', login_required(ListHistorialView), name='historialOrdenes'),
    path('Ordenes/delete/<int:pk>',login_required(DeleteOrdenView.as_view()), name = 'deleteOrden'),
    path('Ordenes/update/<int:pk>',login_required(UpdateOrdenView.as_view()), name = 'updateOrden'),
]