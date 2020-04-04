from django.urls import path,include
from .views import CreateUserView,UpdateUserView,ListUserView,DetailUserView,DeleteUserView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('Registro/crear',login_required(CreateUserView.as_view()),name='createUsuario'),
    path('Registro/update/<int:pk>',login_required(UpdateUserView.as_view()),name='updateUsuario'),
    path('Registro/',login_required(ListUserView.as_view()),name='listViewUsuario'),
    path('',login_required(ListUserView.as_view()),name='listViewUsuario'),

    path('Registro/detail/<int:pk>',login_required(DetailUserView.as_view()),name='detailUsuario'),
    path('Registro/delete/<int:pk>',login_required(DeleteUserView.as_view()),name='deleteUsuario'),
    
]