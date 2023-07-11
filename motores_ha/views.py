from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehiculo, Categoria, Condicion, Reserva
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

#FILTRAR POR CATEGORIA DE AUTO
def automovil(request):
    categoria_automovil = Categoria.objects.get(id=1)
    vehiculos = Vehiculo.objects.filter(categoria=categoria_automovil)
    return render(request, 'motores_ha/autos.html', {'vehiculos': vehiculos})

#FILTRAR POR CATEGORIA DE SUV
def suv(request):
    categoria_suv = Categoria.objects.get(id=2)
    vehiculos = Vehiculo.objects.filter(categoria=categoria_suv)
    return render(request, 'motores_ha/suvs.html', {'vehiculos': vehiculos})

#FILTRAR POR CATEGORIA DE CAMIONETA
def camioneta(request):
    categoria_camioneta= Categoria.objects.get(id=3)
    vehiculos = Vehiculo.objects.filter(categoria=categoria_camioneta)
    return render(request, 'motores_ha/camionetas.html', {'vehiculos': vehiculos})

#FILTRAR POR CONDICION DE NUEVO
def nuevo(request):
    condicion_nuevo = Condicion.objects.get(id=1)
    vehiculos = Vehiculo.objects.filter(condicion=condicion_nuevo)
    return render(request, 'motores_ha/nuevos.html', {'vehiculos': vehiculos})

#FILTRAR POR CONDICION DE USADO
def usado(request):
    condicion_usado = Condicion.objects.get(id=2)
    vehiculos = Vehiculo.objects.filter(condicion=condicion_usado)
    return render(request, 'motores_ha/usados.html', {'vehiculos': vehiculos})

def agregar_al_carrito(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)
    precio_reserva = int(vehiculo.precio * 0.02)  # Calculamos el precio de la reserva (2% del precio del vehículo)
    reserva = Reserva(vehiculo=vehiculo, precio_reserva=precio_reserva)
    reserva.save()
    return redirect('reservas')

def reservas(request):
    reservas = Reserva.objects.all()
    total_reservas = sum(reserva.precio_reserva for reserva in reservas)
    print(reservas)  # Imprime las reservas en la consola
    print(total_reservas)  # Imprime el total de reservas en la consola
    return render(request, 'motores_ha/reservas.html', {'reservas': reservas, 'total_reservas': total_reservas})

def eliminar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    reserva.delete()
    return redirect('reservas')

def login(request):
    return render(request, 'motores_ha/log_in.html')

def signin(request):
    return render(request, 'motores_ha/sign_in.html')
