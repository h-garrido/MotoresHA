from django.db import models

class Condicion(models.Model):
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Transmision(models.Model):
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Traccion(models.Model):
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Combustible(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    nombre = models.CharField(max_length=70)
    condicion = models.ForeignKey(Condicion, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=20)
    version = models.CharField(max_length=20)
    anio = models.IntegerField()
    kilometraje = models.IntegerField()
    transmision = models.ForeignKey(Transmision, on_delete=models.PROTECT)
    traccion = models.ForeignKey(Traccion, on_delete=models.PROTECT)
    combustible = models.ForeignKey(Combustible, on_delete=models.PROTECT)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to = "vehiculos", null=True)

    def __str__(self):
        return self.nombre
    
class Reserva(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    precio_reserva = models.IntegerField()
    estado = models.CharField(max_length=20, default='Pendiente')

    def __str__(self):
        return f"Reserva - {self.vehiculo.nombre}"