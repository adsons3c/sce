from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .models import Setor, Modelos_PC, Computadores, Roteador_Wifi, Impressora
from .models import Switch


class CreatePC(CreateView):
    model = Computadores
    template_name = 'actives_IT/computadores_form.html'
    fields = ['tombamento', 'numero_serie']
