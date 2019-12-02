""" FUNCIONES PARA LA EJECUCIÓN DE LA PREGUNTA 4 - REDES III """
import os 
from twilio.rest import Client

""" ........................ Función para obtener el nivel de un syslog ....................... """
def obtenerNivel(syslog):
    posicion = syslog.find("%")
    bandera = 0
    while bandera != 1:
        if syslog[posicion].isdigit() == True:
            nivel = int(syslog[posicion])
            bandera = 1
        else:
            posicion = posicion + 1
    
    print(" Nivel: %d " % nivel)

    if nivel == 0:
        cadena = " [ NIVEL 0 ] --> [ EMERGENCIA ] \n "
    elif nivel == 1:
        cadena = " [ NIVEL 1 ] --> [ ALERTA ] \n "
    elif nivel == 2:
        cadena = " [ NIVEL 2 ] --> [ CRÍTICA ] \n "
    elif nivel == 3:
        cadena = " [ NIVEL 3 ] --> [ ERROR ] \n "
    elif nivel == 4:
        cadena = " [ NIVEL 4 ] --> [ WARNING ] \n "
    elif nivel == 5:
        cadena = " [ NIVEL 5 ] --> [ NOTIFICACIÓN ] \n "
    elif nivel == 6:
        cadena = " [ NIVEL 6 ] --> [ INFORMACIÓN ] \n "
    elif nivel == 7:
        cadena = " [ NIVEL 7 ] --> [ DEBUG ] \n "
    
    return cadena
""" ..................................................................................... """

""" ........................ Función para mandar un correo ........................ """
def enviarCorreo(nivel, contenido, ip):
    reinicio = " REINICIO DEL ROUTER CON IP: " + ip + "\n"
    mensaje = nivel + reinicio + contenido
    asunto = " ¡ SYSLOG DETECTADO ! "
    comando = "echo \"" + mensaje + "\" | mail -s \"" + asunto + "\" correo_electronico@gmail.com"
    os.system(comando)
    print(" ¡ Notificación de correo enviada !")
""" ..................................................................................... """

""" ........................ Función para mandar un whatsApp ........................ """

def enviarMensaje(nivel, contenido, ip):
    account_sid = ''
    auth_token = ''
    
    reinicio = " REINICIO DEL ROUTER CON IP: " + ip + "\n"
    whatsapp = " ¡ SYSLOG DETECTADO ! \n" + nivel + reinicio + contenido
    cliente = Client(account_sid, auth_token)
    mensaje = cliente.messages.create(
        body = whatsapp,
        from_= 'whatsapp:+',
        to = 'whatsapp:+52155........'
    )
    print(" ¡ Notificación de WhatsApp enviada !")
""" ..................................................................................... """

""" ........................ Función para saber si el syslog corresponde a un reboot ........................ """
def obtenerReinicio(syslog):
    palabra = "STARTSTOP"
    posicion = syslog.find(palabra)
    if posicion >= 0:
        reinicio = 1
    else:
        reinicio = 0
    return reinicio
""" ..................................................................................... """

""" ........................ Función para obtener la IP de un syslog ........................ """
def obtenerIP(syslog):
    inicio = syslog.find("-05:00 ")
    inicio = inicio + 7
    aux = inicio
    while syslog[aux] != ':':
        aux = aux + 1
    
    fin = aux
    ip = syslog[inicio:fin - 2]
    print (ip)
    return ip
""" ..................................................................................... """

""" ....................... Función para eliminar los syslog de la carpeta de origen ................. """
def limpiarDirectorio():
    comando = "mv ../../../var/log/pregunta4/10.1.200.1/*.log /home/zantana/Trash/"
    os.system(comando)
