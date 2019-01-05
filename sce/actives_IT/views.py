from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from .models import Setor, Modelos_PC, Computadores, Roteador_Wifi, Impressora
from .models import Switch
from django.contrib import messages
from django.http import HttpResponse


class CreatePC(CreateView):
    model = Computadores
    template_name = 'actives_IT/computadores_form.html'
    fields = ['tombamento', 'numero_serie', 'sistema_oper', 'licenca_so', 'ip',
              'mac', 'processador', 'memoria', 'hd', 'data_ultima_manutencao',
              'data_proxima_manutencao', 'descricao_manutencao', 'status', 'setor',
              'modelo']

class Create_Modelo_PC(CreateView):
    model = Modelos_PC
    template_name = 'actives_IT/modelo_pc_form.html'
    fields = ['marca', 'modelo']

class Create_Rotetador_Wifi(CreateView):
    model = Roteador_Wifi
    template_name = 'actives_IT/roteador_wifi_form.html'
    fields = ['modelo', 'tombamento', 'numero_serie', 'ip', 'mac', 'senha_admin',
              'data_ultima_manutencao', 'data_proxima_manutencao', 'descricao_manutencao',
              'setor', 'status']

class Create_Setor(CreateView):
    model = Setor
    template_name = 'actives_IT/setor_form.html'
    fields = ['nome', 'sigla']

class Create_Impressora(CreateView):
    model = Impressora
    template_name = 'actives_IT/impressora_form.html'
    fields = ['modelo', 'numero_serie', 'ip', 'locada', 'empresa_locadora', 'data_ultima_manutencao',
              'data_proxima_manutencao', 'descricao_manutencao', 'setor', 'status']

class Create_Switch(CreateView):
    model = Switch
    template_name = 'actives_IT/switch_form.html'
    fields = ['modelo', 'numero_serie', 'ip', 'senha_admin', 'data_ultima_manutencao',
              'data_proxima_manutencao', 'descricao_manutencao', 'setor', 'status']
