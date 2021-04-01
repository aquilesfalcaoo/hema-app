from django import forms
from .models import Doador
from .models import Medico


class DoadorForm(forms.ModelForm):
    class Meta:
        model = Doador
        fields = ['nome', 'CPF', 'tipo_Sanguíneo', 'sexo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['CPF'].widget.attrs.update({'class': 'mask-CPF'})


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nome', 'CRM', 'especialidade']
