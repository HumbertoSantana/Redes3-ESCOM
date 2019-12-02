""" PREGUNTA 3 - REDES III """
import os
import time
from funcionesP3 import *

contendio_original = os.listdir("/var/log/192.168.3.1")

while 1:
    contendio_original.sort()
    tamanio_or = len(contendio_original)
    print(contendio_original)

    contenido_nuevo = os.listdir("/var/log/192.168.3.1")
    contenido_nuevo.sort()
    tamanio_nuevo = len(contenido_nuevo)

    if tamanio_or != tamanio_nuevo:
        print(" ¡¡¡ SYSLOG DETECTADO !!! ")
        diferencia = tamanio_nuevo - tamanio_or
        print(" Original: %d " % tamanio_or )
        print(" Nuevo: %d " % tamanio_nuevo)

        if tamanio_or == 0:
            recorrido = 0
            while recorrido != diferencia:
                print(contenido_nuevo)
                archivo_syslog = open(r"/var/log/192.168.3.1/" + contenido_nuevo[recorrido], "r")
                syslog = archivo_syslog.read()
                print(syslog)
                nivel = obtenerNivel(syslog)
                enviarCorreo(nivel, syslog)
                enviarMensaje(nivel, syslog)

                recorrido = recorrido + 1
                archivo_syslog.close()
            
            contendio_original = contenido_nuevo

        else:
            recorrido = tamanio_or
            print(contenido_nuevo)
            while recorrido != tamanio_nuevo:
                print(contenido_nuevo)
                archivo_syslog = open(r"/var/log/192.168.3.1/" + contenido_nuevo[recorrido], "r")
                syslog = archivo_syslog.read()
                print(syslog)
                nivel = obtenerNivel(syslog)
                enviarCorreo(nivel, syslog)
                enviarMensaje(nivel, syslog)

                recorrido = recorrido + 1
                archivo_syslog.close()
            
            contendio_original = contenido_nuevo
    else:
        print("----------------------------------------")
        time.sleep(1)