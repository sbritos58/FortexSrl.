from django import forms
from .models import Ordenes

class OrdenesForm(forms.ModelForm):
    class Meta:
        model = Ordenes
        fields = ['descripcion','producto','cantidad_recibida','estado','ubicacion','fecha_entrega_estimada','asignado','cantidadEntregada','telaio']



        labels = {
            'cantidadEntregada':'Quantità consegnata',
            'descripcion':"Descrizione",
            'producto':'Prodotto',
            'cantidad_recibida':'Quantità da fare',
            'estado':'Stato',
            'ubicacion':'Ubicazione',
            'fecha_entrega_estimada':'Data di consegna prevista',
            'asignado':'Assegnato a',
        }
        widgets = {
            'cantidadEntregada': forms.NumberInput(attrs={'class':'form-control text-center','id':'CantidadEntregada'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control text-center','id':'descripcion'}),
            'producto': forms.Select(attrs={'class': 'form-control text-center','id':'producto'}),
            'cantidad_recibida': forms.NumberInput(attrs={'class': 'form-control text-center','id':'cantidad_recibida'}),
            'estado': forms.Select(attrs={'class': 'form-control text-center','id':'estado','name':'estado'}),
            'ubicacion': forms.Select(attrs={'class': 'form-control text-center','id':'ubicacion'}),
            'fecha_entrega_estimada': forms.DateInput(attrs={'class': 'form-control text-center','id':'fecha_entregada_estimada'}),
            'asignado': forms.Select(attrs={'class': 'form-control text-center','id':'asignado'}),
            'telaio': forms.NumberInput(attrs={'class': 'form-control text-center', 'id': 'telaio'}),
        }
