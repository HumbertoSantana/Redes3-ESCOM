""" FUNCIONES PARA LA EJECUCIÓN DE LA PREGUNTA 4 - REDES III """
import os 
import smtplib
from email.mime.text import MIMEText
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

""" ..................... Función para enviar un correo electrónico ................ """
def enviarCorreo(nivel, contenido):

    from_addr = "@gmail.com"
    to_addr = ""

    mensaje = MIMEText("¡ Syslog detectado ! \n " + nivel + contenido)
    mensaje['From'] = from_addr
    mensaje['To'] = to_addr
    mensaje['Subject'] = "Syslog detectado"

    username = ""
    password = ""

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(username, password)
    server.sendmail(from_addr, to_addr, mensaje.as_string())
    server.quit()
    print(" ¡ Notificación de correo enviada !")
""" ......................................................................................................"""

""" ........................ Función para mandar un whatsApp ........................ """

def enviarMensaje(nivel, contenido):
    account_sid = ''
    auth_token = ''

    whatsapp = " ¡ SYSLOG DETECTADO ! \n" + nivel + contenido
    cliente = Client(account_sid, auth_token)
    mensaje = cliente.messages.create(
        body = whatsapp,
        from_= 'whatsapp:+',
        to = 'whatsapp:+521'
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
