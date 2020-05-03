from django.urls import path,include
from .views import ListViewStock,CreateViewStock,CreateView,UpdateStock,ListViewMovimientosStock
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('Stock/',login_required(ListViewStock),name='listStock'),
    path('Stock/update/<int:pk>', login_required(UpdateStock.as_view()), name='updateStock'),
    path('Stock/crear',login_required(CreateViewStock),name='crearStock'),
    path('Stock/crear2/<str:pk>/', login_required(CreateView), name='crearStock2'),
    path('Stock/listMov/', login_required(ListViewMovimientosStock), name='listMov'),

]