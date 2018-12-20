from django.urls import path
from .views import CreatePC


urlpatterns = [
    path('adicionarpc/', CreatePC.as_view(), name='adicionarpc'),
]
