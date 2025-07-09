from django.urls import path
from .views import *

app_name = 'reseñas'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('reseña/crear/', crear_reseña, name='crear_reseña'),
    path('truco/agregar/', agregar_truco, name='agregar_truco'),
    path('consola/agregar/', agregar_consola, name='agregar_consola'),
]
