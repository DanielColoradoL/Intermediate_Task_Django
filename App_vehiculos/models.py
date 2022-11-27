from django.db import models

class Carros(models.Model):
    nombre = models.CharField(max_length=20)
    fabricante = models.CharField(max_length=20)
    modelo = models.IntegerField()
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre +" del fabricante "+ self.fabricante


class Motos(models.Model):
    nombre = models.CharField(max_length=20)
    fabricante = models.CharField(max_length=20)
    cilindraje = models.IntegerField()

    def __str__(self):
        return self.nombre +" del fabricante "+ self.fabricante

class Camiones(models.Model):
    nombre = models.CharField(max_length=20)
    fabricante = models.CharField(max_length=20)
    carga_maxima = models.IntegerField()
    numero_ejes = models.IntegerField()

    def __str__(self):
        return self.nombre +" del fabricante "+ self.fabricante