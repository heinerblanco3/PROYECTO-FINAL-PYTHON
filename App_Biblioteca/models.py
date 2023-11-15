from django.db import models

# Create your models here.
class DatosContacto(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=50)
    email=models.CharField(max_length=9)

c1=DatosContacto(nombre="Juan",direccion="Calle 1",telefono="123456789",email="juan@gmail.com")   