from django.urls import path,include
from .views import ListViewStock,CreateViewStock
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('Stock/',login_required(ListViewStock),name='listStock'),
    path('Stock/crear',login_required(CreateViewStock),name='crearStock'),
]