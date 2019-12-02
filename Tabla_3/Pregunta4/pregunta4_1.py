""" PREGUNTA 4 - REDES III """
import os
import time
from funcionesP4 import *

contendio_original = os.listdir("/var/log/10.0.1.1")

while 1:
    contendio_original.sort()
    tamanio_or = len(contendio_original)
    print(contendio_original)

    contenido_nuevo = os.listdir("/var/log/10.0.1.1")
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
                archivo_syslog = open(r"/var/log/10.0.1.1/" + contenido_nuevo[recorrido], "r")
                syslog = archivo_syslog.read()
                print(syslog)
                nivel = obtenerNivel(syslog)
                reinicio = obtenerReinicio(syslog)
                if reinicio == 1:
                    ip = obtenerIP(syslog)
                    #enviarCorreo(nivel, syslog, ip)
                    enviarMensaje(nivel, syslog, ip)
                    recorrido = recorrido + 1
                    archivo_syslog.close()
                else:
                    recorrido = recorrido + 1
                    archivo_syslog.close()
            contendio_original = contenido_nuevo

    else:
        print("----------------------------------------")
        time.sleep(1)
