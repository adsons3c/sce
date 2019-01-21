from django import forms
from .models import *


class GetSetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = ["sigla"]
