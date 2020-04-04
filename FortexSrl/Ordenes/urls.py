from django.urls import path,include
from .views import CreateOrdenView,ListOrdenView,DetailOrdenView,DeleteOrdenView,UpdateOrdenView

urlpatterns = [
    path('Ordenes/crear/',CreateOrdenView.as_view(),name='crearOrden'),
    path('Ordenes/',ListOrdenView.as_view(),name = 'listarOrden'),
    path('Ordenes/detail/<int:pk>',DetailOrdenView.as_view(), name = 'detailOrden'),
    path('Ordenes/delete/<int:pk>',DeleteOrdenView.as_view(), name = 'deleteOrden'),
    path('Ordenes/update/<int:pk>',UpdateOrdenView.as_view(), name = 'updateOrden'),
]