from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('todos-los-vehiculos', views.todos_los_vehiculos, name='todos-los-vehiculos'),
    path('agregar-vehiculo', views.agregar_vehiculo, name='agregar-vehiculo'),
    path('listar-vehiculo', views.listar_vehiculo, name='listar-vehiculo'),
    path('modificar-vehiculo/<id>', views.modificar_vehiculo, name='modificar-vehiculo'),
    path('eliminar-vehiculo/<id>', views.eliminar_vehiculo, name='eliminar-vehiculo'),



]