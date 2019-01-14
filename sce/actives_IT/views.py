from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Setor, Modelos_PC, Computadores, Roteador_Wifi, Impressora
from .models import Switch, Range_Ips_Setor
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError


class Home(TemplateView):
    template_name = "actives_IT/home.html"

class CreatePC(CreateView):
    model = Computadores
    template_name = 'actives_IT/computadores_form.html'
    fields = ['setor', 'modelo','tombamento', 'numero_serie', 'sistema_oper', 'licenca_so', 'ip',
              'mac', 'processador', 'memoria', 'hd', 'data_ultima_manutencao',
              'data_proxima_manutencao', 'descricao_manutencao', 'status',]

    success_url = '/adicionarpc/'

class Create_Modelo_PC(CreateView):
    model = Modelos_PC
    template_name = 'actives_IT/modelo_pc_form.html'
    fields = ['marca', 'modelo']

    def form_valid(self,form):
        try:
            form.save()
            return HttpResponseRedirect('/home/')
        except IntegrityError:
            return HttpResponse("Duplicado")
    success_url = '/adicionarmodelopc/'




class Create_Rotetador_Wifi(CreateView):
    model = Roteador_Wifi
    template_name = 'actives_IT/roteador_wifi_form.html'
    fields = ['modelo', 'tombamento', 'numero_serie', 'ip', 'mac', 'senha_admin',
              'data_ultima_manutencao', 'data_proxima_manutencao', 'descricao_manutencao',
              'setor', 'status']

    success_url = '/adicionarroteadorwifi/'

class Create_Setor(CreateView):
    model = Setor
    template_name = 'actives_IT/setor_form.html'
    fields = ['nome', 'sigla', 'range_inicial', 'range_final']
    success_url = '/adicionarsetor/'

class Create_Impressora(CreateView):
    model = Impressora
    template_name = 'actives_IT/impressora_form.html'
    fields = ['modelo', 'numero_serie', 'ip', 'locada', 'empresa_locadora', 'data_ultima_manutencao',
              'data_proxima_manutencao', 'descricao_manutencao', 'setor', 'status']
    success_url = '/adicionarimpressora/'

class Create_Switch(CreateView):
    model = Switch
    template_name = 'actives_IT/switch_form.html'
    fields = ['modelo', 'numero_serie', 'ip', 'senha_admin', 'data_ultima_manutencao',
              'data_proxima_manutencao', 'descricao_manutencao', 'setor', 'status']
    success_url = '/adicionarswitch/'

class Create_Range_Setor(CreateView):
    model = Range_Ips_Setor
    template_name = 'actives_IT/Range_Ips_Setor_form.html'
    fields = ['setor', 'range_inicial', 'range_final']
