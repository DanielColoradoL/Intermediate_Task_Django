from django.urls import path
from App_vehiculos.views import *

urlpatterns = [
    path("", inicio, name= "inicio"),
    path("agregarcarros", agregar_carros, name= "agregar_carros"),
    path("agregarmotos", agregar_motos, name= "agregar_motos"),
    path("agregarcamiones", agregar_camiones, name= "agregar_camiones"),
    path("busqueda", busqueda_db, name= "busqueda_db"),          
]