from random import choice
from django.db import models

# Create your models here.
class Municipio(models.Model):

    CodigoMunicipio = models.PositiveSmallIntegerField()
    NombreMunicipio = models.CharField(max_length = 35)
    EstadosMunicipios = (('A', 'Activo'), ('I', 'Inactivo'))
    EstadoMunicipio = models.CharField(max_length=1, choices=EstadosMunicipios, default='A')

    def informacionMunicipio(self):
        cadena = "{0}"
        return cadena.format( self.NombreMunicipio)

    def __str__(self):
        return self.informacionMunicipio()

class Region(models.Model):
    CodigoRegion = models.PositiveSmallIntegerField()
    NombreRegion = models.CharField(max_length=35)
    EstadosRegiones= (('A', 'Activo'), ('I', 'Inactivo'))
    EstadoRegion = models.CharField(max_length=1, choices=EstadosRegiones, default='A')
    #Relaciones
    Municipio = models.ManyToManyField(Municipio, blank=True)

    def informacionRegion(self):
        cadena = "{0}";
        return cadena.format(self.NombreRegion)

    def __str__(self):
        return self.informacionRegion()