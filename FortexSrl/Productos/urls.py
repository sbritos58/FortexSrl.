from django.urls import path,include
from .views import CreateProductosView,ListProductosView,UpdateProductosView,DeleteProductosView,DetailProductosView
urlpatterns = [
    path('Productos/create',CreateProductosView.as_view(),name='createProductos'),
    path('Productos/', ListProductosView.as_view(), name='listProductos'),
    path('Productos/update/<int:pk>', UpdateProductosView.as_view(), name='updateProductos'),
    path('Productos/detail/<int:pk>',DetailProductosView.as_view(), name='detailProductos'),
    path('Productos/delete/<int:pk>',DeleteProductosView.as_view(), name='deleteProductos'),
]
