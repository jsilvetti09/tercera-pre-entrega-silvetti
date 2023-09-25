from django.urls import path
from .views import *

urlpatterns = [
    path("", inicio, name ="inicio"),
    path("jugadores/", ver_jugadores, name ="ver_jugadores"),
    path("futbol/", ver_futbol, name = "ver_futbol" ),
    path("basquet/", ver_basquet, name ="ver_basquet"),
    path("rugby/", ver_rugby, name ="ver_rugby"),
    path("crearjugador/", crear_jugador, name = "CrearJugadores"),
    path("crearfutbol/", crear_futbol, name ="CrearFutbol"),
    path("crearbasquet/", crear_basquet, name ="CrearBasquet"),
    path("buscarjugador/", buscar_jugador, name = "BuscarJugador"),
    path("resultadojugador/", resultadojugador, name = "ResultadoJugador"),
    path("buscarfutbol/", buscar_futbol, name= "BuscarFutbol"),
    path("resultadofutbol/", resultado_futbol, name="ResultadoFutbol"),
    path("buscarbasquet/", buscar_basquet, name= "BuscarBasquet"),
    path("resultadobasquet/", resultado_basquet, name = "ResultadoBasquet"),
    path("buscarrugby/", buscar_rugby, name = "BuscarRugby"),
    path("crearrugby/", crear_rugby, name = "CrearRugby"),
    path("resultadorugby/", resultado_rugby, name = "ResultadoRugby"),
]
