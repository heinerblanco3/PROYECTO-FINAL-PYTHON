from django.shortcuts import render, HttpResponse
from django.template import Template,Context
import datetime
from django.template import loader
from django.shortcuts import render
from .models import Libro

# Create your views here. first create a landing page about the library

def landing_page(request):
    return render(request, 'partes/body.html')

def paginaReservas(request):
    return render(request, 'partes/paginaReservas.html')

def paginaContactanos(request):
    return render(request, 'partes/paginaContactanos.html')

def paginaMiCarrito(request):
    return render(request, 'partes/paginaMiCarrito.html')

def paginaInicio(request):
    return render(request, 'partes/body.html')

def paginaLibros(request):
    libros=Libro.objects.all()
    data={'libros':libros}
    
    return render(request, 'partes/paginaLibros.html')


#Reservación: El objetivo de esta view, es mostrar todos los libros que contiene la Biblioteca (Tener en la Base de Datos ya guardados unos 30 como mínimo para el demo), y mostrar los libros: su título, su imagen y su botón de agregar. Se debe de utilizar paginación para indicar en que página se encuentra uno y la cantidad de libros a mostrar por página. El botón “agregar”, debe de ser un POST, y cuando se agregan ya no deben de aparecer más, porque se le debe de cambiar su estado de disponible True a False y renderizar la misma pagina en la que se encuentra

class Libro:
    def __init__(self, titulo, autor, imagen, disponible):
        self.titulo = titulo
        self.autor = autor
        self.imagen = imagen
        self.disponible = disponible
        
def datos_Contacto(request):
    return render(request, 'partes/footer.html')    