from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'endereco', 'bairro', 'cidade', 'telefone']
        widgets = {
            'telefone': forms.TextInput(attrs={'required': True}),
            'cpf': forms.TextInput(attrs={'required': True}),
        }
