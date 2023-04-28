from django import forms
from .models import Aluguel, Item

class AluguelForm(forms.ModelForm):
    itens_alugados = forms.ModelMultipleChoiceField(
        queryset=Item.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Aluguel
        fields = ['cliente', 'data_aluguel', 'valor', 'itens_alugados']

    def clean_itens_alugados(self):
        itens_alugados = self.cleaned_data['itens_alugados']
        if not itens_alugados:
            raise forms.ValidationError('Selecione pelo menos um item para alugar')
        return itens_alugados

