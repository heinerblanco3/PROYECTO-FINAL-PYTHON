
from django.urls import path
from App_Biblioteca import views
from django.urls import path,include


urlpatterns = [
    path ('', views.landing_page, name='home'),
    path('reservarLibros', views.paginaReservas, name='reservarLibros'),
    path('contactanos', views.paginaContactanos, name='contactanos'),
    path('miCarrito', views.paginaMiCarrito, name='miCarrito'),
    path('inicio', views.paginaInicio, name='inicio'),
]

