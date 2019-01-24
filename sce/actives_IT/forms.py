from django import forms
from .models import *


class GetSetorForm(forms.Form):
    sigla = forms.ModelChoiceField(Setor.objects.order_by("sigla"))
