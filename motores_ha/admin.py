from django.contrib import admin
from .models import Marca, Transmision, Traccion, Combustible, Vehiculo

admin.site.register(Marca)
admin.site.register(Transmision)
admin.site.register(Traccion)
admin.site.register(Combustible)
admin.site.register(Vehiculo)