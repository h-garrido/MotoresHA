from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehiculo
from .forms import VehiculoForm

# Create your views here.
def home(request):
    return render(request, 'motores_ha/index.html')

def todos_los_vehiculos(request):

    #select * from vehiculo
    vehiculos = Vehiculo.objects.all()
    data = {"vehiculos": vehiculos}
    return render(request, 'motores_ha/todos_los_vehiculos.html', data)

def agregar_vehiculo(request):
    data = {"form": VehiculoForm()}

    if request.method == "POST":
        formulario = VehiculoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data['form'] = formulario 

    return render(request, 'motores_ha/vehiculo/agregar.html', data)

def listar_vehiculo(request):
    vehiculos = Vehiculo.objects.all()
    data = {"vehiculos": vehiculos}
    return render(request, 'motores_ha/vehiculo/listar.html', data)

#select * from vehiculo where id = id
def modificar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    data = {'form': VehiculoForm(instance=vehiculo)}

    if request.method == "POST":
        formulario = VehiculoForm(data=request.POST, instance=vehiculo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Vehiculo guardado correctamente"
            return redirect(to = "listar-vehiculo")
        else:
            data['form'] = formulario 

    return render(request, 'motores_ha/vehiculo/modificar.html', data)

def eliminar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    vehiculo.delete()
    return redirect(to = "listar-vehiculo")