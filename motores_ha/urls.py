from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('todos-los-vehiculos', views.todos_los_vehiculos, name='todos-los-vehiculos'),
    path('agregar-vehiculo', views.agregar_vehiculo, name='agregar-vehiculo'),
    path('listar-vehiculo', views.listar_vehiculo, name='listar-vehiculo'),
    path('modificar-vehiculo/<id>', views.modificar_vehiculo, name='modificar-vehiculo'),
    path('eliminar-vehiculo/<id>', views.eliminar_vehiculo, name='eliminar-vehiculo'),
    path('categoria-auto', views.automovil, name='categoria-auto'),
    path('categoria-suv', views.suv, name='categoria-suv'),
    path('categoria-camioneta', views.camioneta, name='categoria-camioneta'),
    path('condicion-nuevo', views.nuevo, name='condicion-nuevo'),
    path('condicion-usado', views.usado, name='condicion-usado'),
    path('agregar-al-carrito/<int:vehiculo_id>/', views.agregar_al_carrito, name='agregar-al-carrito'),
    path('reservas/', views.reservas, name='reservas'),
    path('eliminar-reserva/<int:reserva_id>/', views.eliminar_reserva, name='eliminar-reserva'),
    path('log-in', views.login, name='log-in'),
    path('sign-in', views.signin, name='sign-in'),

]