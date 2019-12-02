""" PREGUNTA 1 - TABLA 4 - REDES III """ 
from funcionesP1 import * 

direcciones_telnet = ['10.1.200.1', '10.5.200.1', '10.7.200.1', '10.8.200.1', '10.9.200.1', '10.12.200.1', '10.11.200.2', '10.13.200.1', '10.14.200.1', '10.15.200.1']


for direccion in direcciones_telnet:
    buffer = extraerInformacion(direccion)
    id_router = extraerID(buffer)
    contenido = extraerInformacionHardware(buffer, id_router)   
    enviarWhats(id_router, direccion, contenido)
    enviarCorreo(id_router, direccion, contenido)
