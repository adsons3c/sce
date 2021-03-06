from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Setor, Modelos_PC, Computadores, Roteador_Wifi, Impressora
from .models import Switch
from django.contrib import messages
from django.http import HttpResponse
from django.db import IntegrityError
from .forms import GetSetorForm



class Home(TemplateView):
    template_name = "actives_IT/home.html"

class CreatePC(CreateView):
    model = Computadores
    template_name = 'actives_IT/computadores_form.html'
    fields = ['tombamento', 'numero_serie', 'sistema_oper', 'licenca_so', 'ip',
              'mac', 'processador', 'memoria', 'hd', 'data_ultima_manutencao',
              'data_proxima_manutencao', 'descricao_manutencao','setor','modelo','status',]

    def form_valid(self,form):
        try:
            form.save()
            return render(self.request, 'actives_IT/home.html')
        except IntegrityError:
            return HttpResponse("Duplicado")


class Create_Modelo_PC(CreateView):
    model = Modelos_PC
    template_name = 'actives_IT/modelo_pc_form.html'
    fields = ['marca', 'modelo']


    def form_valid(self,form):
        try:
            form.save()
            return render(self.request, 'actives_IT/home.html')
        except IntegrityError:
            return HttpResponse("Duplicado")


class Create_Rotetador_Wifi(CreateView):
    model = Roteador_Wifi
    template_name = 'actives_IT/roteador_wifi_form.html'
    fields = ['modelo', 'tombamento', 'numero_serie', 'ip', 'mac', 'senha_admin',
              'data_ultima_manutencao', 'data_proxima_manutencao', 'descricao_manutencao',
              'setor', 'status']

    def form_valid(self,form):
        try:
            form.save()
            return render(self.request, 'actives_IT/home.html')
        except IntegrityError:
            return HttpResponse("Duplicado")


class Create_Setor(CreateView):
    model = Setor
    template_name = 'actives_IT/setor_form.html'
    fields = ['nome', 'sigla']

    def form_valid(self,form):
        try:
            form.save()
            return render(self.request, 'actives_IT/home.html')
        except IntegrityError:
            return HttpResponse("Duplicado")


class Create_Impressora(CreateView):
    model = Impressora
    template_name = 'actives_IT/impressora_form.html'
    fields = ['modelo', 'tombamento','numero_serie', 'ip', 'locada', 'empresa_locadora', 'data_ultima_manutencao',
              'data_proxima_manutencao', 'descricao_manutencao', 'setor', 'status']

    def form_valid(self,form):
        try:
            form.save()
            return render(self.request, 'actives_IT/home.html')
        except IntegrityError:
            return HttpResponse("Duplicado")

class Create_Switch(CreateView):
    model = Switch
    template_name = 'actives_IT/switch_form.html'
    fields = ['modelo','tombamento','numero_serie', 'ip', 'senha_admin', 'data_ultima_manutencao',
              'data_proxima_manutencao', 'descricao_manutencao', 'setor', 'status']

    def form_valid(self,form):
        try:
            form.save()
            return render(self.request, 'actives_IT/home.html')
        except IntegrityError:
            return HttpResponse("Duplicado")


'''Definição das class ListView'''

class PC_List(ListView):
    model = Computadores
    template_name = 'actives_IT/computadores_list.html'
    paginate_by = 20


class Modelos_PC_List(ListView):
    model = Modelos_PC
    template_name = 'actives_IT/modelos_pc_list.html'
    paginate_by = 20


class Roteador_Wifi_List(ListView):
    model = Roteador_Wifi
    template_name = 'actives_IT/roteador_wifi_list.html'
    paginate_by = 20


class Setor_List(ListView):
    model = Setor
    template_name = 'actives_IT/setor_list.html'
    paginate_by = 20


class Impressora_List(ListView):
    model = Impressora
    template_name = 'actives_IT/impressora_list.html'
    paginate_by = 20


class Switch_List(ListView):
    model = Switch
    template_name = 'actives_IT/switch_list.html'
    paginate_by = 20



'''Definição das Class DetailView'''

class PC_Detail(DetailView):
    model = Computadores

class Modelo_PC_Detail(DetailView):
    model = Modelos_PC

class Roteador_Wifi_Detail(DetailView):
    model = Roteador_Wifi

class Setor_Detail(DetailView):
    model = Setor

class Impressora_Detail(DetailView):
    model = Impressora

class Switch_Detail(DetailView):
    model = Switch


'''Lista de IPs Ativos'''
def listaipsativos(request):
    form = GetSetorForm()
    if request.method == "POST":
        form = GetSetorForm(request.POST)
        if form.is_valid():
            formulario = form.cleaned_data["sigla"]
            ipspc = Computadores.objects.filter(setor__sigla = formulario.sigla)
            ipsimp = Impressora.objects.filter(setor__sigla = formulario.sigla)
            ipsroute = Roteador_Wifi.objects.filter(setor__sigla = formulario.sigla)
            ipssw = Switch.objects.filter(setor__sigla = formulario.sigla)
            rangeips = Range_Ips_Setor.objects.filter(setor__sigla = formulario.sigla)

    return render (request, 'actives_IT/listaipsativos.html', locals())


'''Função para listar dos os Equipamentos por Setor'''
def listaequip(request):
    form = GetSetorForm()
    if request.method == "POST":
        form = GetSetorForm(request.POST)
        if form.is_valid():
            formulario = form.cleaned_data["sigla"]
            C = Computadores.objects.filter(setor__sigla = formulario.sigla)
            I = Impressora.objects.filter(setor__sigla = formulario.sigla)
            RW = Roteador_Wifi.objects.filter(setor__sigla = formulario.sigla)
            SW = Switch.objects.filter(setor__sigla = formulario.sigla)

    return render (request, 'actives_IT/listasetores.html', locals())
