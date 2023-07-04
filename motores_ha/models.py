from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=30)

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
    precio = models.IntegerField()
    modelo = models.CharField(max_length=20)
    version = models.CharField(max_length=10)
    anio = models.IntegerField()
    kilometraje = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    transmision = models.ForeignKey(Transmision, on_delete=models.PROTECT)
    traccion = models.ForeignKey(Traccion, on_delete=models.PROTECT)
    combustible = models.ForeignKey(Combustible, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to = "vehiculos", null=True)

    def __str__(self):
        return self.nombre