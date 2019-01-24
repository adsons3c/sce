from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('adicionarpc/', CreatePC.as_view(), name='adicionarpc'),
    path('adicionarmodelopc/', Create_Modelo_PC.as_view(), name='adicionarmodelopc'),
    path('adicionarroteadorwifi/', Create_Rotetador_Wifi.as_view(), name='adicionarroteadorwifi'),
    path('adicionarsetor/', Create_Setor.as_view(), name='adicionarsetor'),
    path('adicionarimpressora/', Create_Impressora.as_view(), name='adicionarimpressora'),
    path('adicionarswitch/', Create_Switch.as_view(), name='adicionarswitch'),
    path('listapcs', PC_List.as_view(), name='listapcs'),
    path('listamodelepc', Modelos_PC_List.as_view(), name='listamodelepc'),
    path('listaroteadorwifi', Roteador_Wifi_List.as_view(), name='listaroteadorwifi'),
    path('listasetor', Setor_List.as_view(), name='listasetor'),
    path('listaimpressora', Impressora_List.as_view(), name='listaimpressora'),
    path('listaswitch', Switch_List.as_view(), name='listaswitch'),
    path('listarangeips', Range_Ips_Setor_List.as_view(), name='listarangeips'),
    path('detalhespc/<int:pk>/', PC_Detail.as_view(), name='detalhespc'),
    path('detalhesmodelopc/<int:pk>/', Modelo_PC_Detail.as_view(), name='detalhesmodelopc'),
    path('detalhesroteadorwifi/<int:pk>/', Roteador_Wifi_Detail.as_view(), name='detalhesroteadorwifi'),
    path('detalhessetor/<int:pk>/', Setor_Detail.as_view(), name='detalhessetor'),
    path('detalhesimpressora/<int:pk>/', Impressora_Detail.as_view(), name='detalhesimpressora'),
    path('detalhesswitch/<int:pk>/', Switch_Detail.as_view(), name='detalhesswitch'),
    path('detalhesrangeips/<int:pk>/', Range_Ips_Setor_Detail.as_view(), name='detalhesrangeips'),
    path('adicionarrangeipssetor/', Create_Range_Setor.as_view(), name='adicionarrangeipssetor'),
    path('listaequisetor/', views.listaequip, name='listaequisetor')
]
