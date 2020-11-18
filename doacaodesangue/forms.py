from django import forms
from .models import Doador
from .models import Medico

class DoadorForm(forms.ModelForm):
    class Meta:
        model = Doador
        fields = ['nome', 'RG', 'tipo_Sanguíneo', 'gênero']

class MedicoForm(forms.ModelForm):
    class Meta:
      model = Medico
      fields = ['nome', 'CRM', 'especialidade']