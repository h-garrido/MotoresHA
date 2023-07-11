from django.contrib import admin
from .models import Condicion, Categoria, Transmision, Traccion, Combustible, Vehiculo

admin.site.register(Condicion)
admin.site.register(Categoria)
admin.site.register(Transmision)
admin.site.register(Traccion)
admin.site.register(Combustible)
admin.site.register(Vehiculo)