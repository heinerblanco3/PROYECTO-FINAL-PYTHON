from django.db import models

# Create your models here.
class DatosContacto(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=50)
    email=models.CharField(max_length=9)

c1=DatosContacto(nombre="Juan",direccion="Calle 1",telefono="123456789",email="juan@gmail.com")   

class Libro(models.Model):
    titulo=models.CharField(max_length=50)
    autor=models.CharField(max_length=50)
    imagen=models.CharField(max_length=50)
    disponible=models.BooleanField(default=True)

l1=Libro(titulo="El principito",autor="Antoine de Saint-Exupéry",imagen="https://images-na.ssl-images-amazon.com/images/I/51QXWVezmdL._SX331_BO1,204,203,200_.jpg",disponible=True)
l2=Libro(titulo="El señor de los anillos",autor="J.R.R. Tolkien",imagen="https://images-na.ssl-images-amazon.com/images/I/51QXWVezmdL._SX331_BO1,204,203,200_.jpg",disponible=True)
l3=Libro(titulo="El código Da Vinci",autor="Dan Brown",imagen="https://images-na.ssl-images-amazon.com/images/I/51QXWVezmdL._SX331_BO1,204,203,200_.jpg",disponible=True)
l4=Libro(titulo="El alquimista",autor="Paulo Coelho",imagen="https://images-na.ssl-images-amazon.com/images/I/51QXWVezmdL._SX331_BO1,204,203,200_.jpg",disponible=True)