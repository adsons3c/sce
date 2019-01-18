from django.contrib import admin
from .models import Computadores, Impressora, Roteador_Wifi, Switch, Setor, Modelos_PC, Range_Ips_Setor

admin.site.register(Computadores)
admin.site.register(Impressora)
admin.site.register(Roteador_Wifi)
admin.site.register(Switch)
admin.site.register(Setor)
admin.site.register(Modelos_PC)
admin.site.register(Range_Ips_Setor)
