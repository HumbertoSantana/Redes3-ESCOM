""" REDES III - PREGUNTA 2 """
from funcionesP2 import *

mostrarUltimaSolicitud()
respuesta = mostrarPregunta() 

while respuesta == 1:
    update = obtenerConfiguraciones() 
    enviarWhats(update)
    enviarCorreo(update)
    mostrarUltimaSolicitud()
    respuesta = mostrarPregunta()
if respuesta == 2:
    terminarEjecucion()  