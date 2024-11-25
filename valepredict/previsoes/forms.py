from django import forms
from .models import DadosAgricolas

class PrevisaoForm(forms.Form):
    nome_cultura = forms.ModelChoiceField(queryset=DadosAgricolas.objects.all(), 
                                          to_field_name='cultura', 
                                          label="Escolha a cultura")
    area = forms.DecimalField(label="Área disponível para plantio (hectares)", max_digits=10, decimal_places=2)
