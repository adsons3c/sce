from django.urls import path
from .views import *


urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('adicionarpc/', CreatePC.as_view(), name='adicionarpc'),
    path('adicionarmodelopc/', Create_Modelo_PC.as_view(), name='adicionarmodelopc'),
    path('adicionarroteadorwifi/', Create_Rotetador_Wifi.as_view(), name='adicionarroteadorwifi'),
    path('adicionarsetor/', Create_Setor.as_view(), name='adicionarsetor'),
    path('adicionarimpressora/', Create_Impressora.as_view(), name='adicionarimpressora'),
    path('adicionarswitch/', Create_Switch.as_view(), name='adicionarswitch'),
    path('adicionarrangeipssetor/', Create_Range_Setor.as_view(), name='adicionarrangeipssetor'),
]
