from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        #fields = ['nombre', disponible]   podemos seleccionar que campos queremos manejar
        fields = "__all__"