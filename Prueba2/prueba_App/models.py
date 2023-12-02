from django.db import models

# Create your models here.

class Socios(models.Model):
    Socio_Nombre = models.CharField(max_length=80)
    Socio_Fecha_in = models.DateField()
    Socio_Anio = models.IntegerField()
    Socio_Telefono = models.IntegerField()
    Socio_Email = models.EmailField()
    Socio_Sexo = models.CharField(max_length=30)
    Socio_Estado = models.CharField(max_length=30)
    Socio_Observacion = models.CharField(max_length=100,blank=True)
