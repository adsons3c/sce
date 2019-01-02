from django.urls import path
from .views import *


urlpatterns = [
    path('adicionarpc/', CreatePC.as_view(), name='adicionarpc'),
    path('adicionarmodelopc/', Create_Modelo_PC.as_view(), name='adicionarmodelopc'),
    path('adicionarroteadorwifi/', Create_Rotetador_Wifi.as_view(), name='adicionarroteadorwifi'),
    path('adicionarsetor/', Create_Setor.as_view(), name='adicionarsetor'),
    path('adicionarsetor/', Create_Impressora.as_view(), name='adicionarsetor'),
]
