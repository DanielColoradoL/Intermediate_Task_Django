from django.shortcuts import render
from .models import Carros, Motos, Camiones
from .forms import CarrosForm, MotosForm, CamionesForm

def inicio(request):
    return render(request, "inicio.html")


def agregar_carros(request):
    if request.method == "POST":
        form_carro_info = CarrosForm(request.POST)
        if form_carro_info.is_valid():
            datos = form_carro_info.cleaned_data
            carro_nuevo = Carros(nombre = datos["nombre"], fabricante = datos["fabricante"], modelo = datos["modelo"], color = datos["color"])
            carro_nuevo.save()
            return render(request, "agregar_carros.html", {"form_carro":CarrosForm()})
    else:
        formulario_vacio = CarrosForm()
        return render(request, "agregar_carros.html", {"form_carro":formulario_vacio})


def agregar_motos(request):
    return render(request, "agregar_motos.html")

def agregar_camiones(request):
    return render(request, "agregar_camiones.html")

def busqueda_db(request):
    return render(request, "busqueda.html")