from django import forms
from .models import Stock,StockMovimientos

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'

class StockMovimientosForm(forms.ModelForm):
    class Meta:
        model = StockMovimientos
        fields = '__all__'

        def clean_cantidad(self):
            cantidad = self.cleaned_data['cantidad']
            if cantidad == "":
                raise forms.ValidationError("Inserisci un valore valido")
            return cantidad

