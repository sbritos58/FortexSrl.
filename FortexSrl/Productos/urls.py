from django.urls import path,include
from .views import CreateProductosView,ListProductosView,UpdateProductosView,DeleteProductosView,DetailProductosView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('Productos/create',login_required(CreateProductosView.as_view()),name='createProductos'),
    path('Productos/', login_required(ListProductosView), name='listProductos'),
    path('Productos/update/<int:pk>', login_required(UpdateProductosView.as_view()), name='updateProductos'),
    path('Productos/detail/<int:pk>',login_required(DetailProductosView.as_view()), name='detailProductos'),
    path('Productos/delete/<int:pk>',login_required(DeleteProductosView.as_view()), name='deleteProductos'),
]
