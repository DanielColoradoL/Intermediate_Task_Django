from django.shortcuts import render
from .models import Carros, Motos, Camiones
from .forms import CarrosForm, MotosForm, CamionesForm

def inicio(request):
    return render(request, "inicio.html", {"mensaje_inicio": "Bienvenido!"})


def agregar_carros(request):
    if request.method == "POST":
        form_carro_info = CarrosForm(request.POST)
        if form_carro_info.is_valid():
            datos = form_carro_info.cleaned_data
            carro_nuevo = Carros(nombre = datos["nombre"], fabricante = datos["fabricante"], modelo = datos["modelo"], color = datos["color"])
            carro_nuevo.save()
            return render(request, "inicio.html", {"mensaje_inicio": "El vehiculo ha sido agregado exitosamente!"})
    else:
        formulario_vacio = CarrosForm()
        return render(request, "agregar_carros.html", {"form_carro":formulario_vacio})


def agregar_motos(request):
    if request.method == "POST":
        form_moto_info = MotosForm(request.POST)
        if form_moto_info.is_valid():
            datos = form_moto_info.cleaned_data
            moto_nueva = Motos(nombre = datos["nombre"], fabricante = datos["fabricante"], cilindraje = datos["cilindraje"])
            moto_nueva.save()
            return render(request, "inicio.html", {"mensaje_inicio": "El vehiculo ha sido agregado exitosamente!"})
    else:
        formulario_vacio = MotosForm()
        return render(request, "agregar_motos.html", {"form_moto":formulario_vacio})    


def agregar_camiones(request):
    if request.method == "POST":
        form_camion_info = CamionesForm(request.POST)
        if form_camion_info.is_valid():
            datos = form_camion_info.cleaned_data
            camion_nuevo = Camiones(nombre = datos["nombre"], fabricante = datos["fabricante"], carga_maxima = datos["carga_maxima"], numero_ejes = datos["numero_ejes"])
            camion_nuevo.save()
            return render(request, "inicio.html", {"mensaje_inicio": "El vehiculo ha sido agregado exitosamente!"})
    else:
        formulario_vacio = CamionesForm()
        return render(request, "agregar_camiones.html", {"form_camion":formulario_vacio})


def busqueda_db(request):
    return render(request, "busqueda_db.html", {"mensaje_busqueda":"Seleccione un fabricante"})


def resultado_busqueda(request):
    valor_url = request.GET["Fabricante"]
    if valor_url != "":
        if valor_url != "*":
            motos_filtradas = Motos.objects.filter(fabricante = valor_url)
        else:
            motos_filtradas = Motos.objects.all()
        return render(request, "resultado_busqueda.html", {"motos_seleccionadas":motos_filtradas})
    else:
        return render(request, "busqueda_db.html", {"mensaje_busqueda": "Vuelva a intentarlo, valor vacio"})
