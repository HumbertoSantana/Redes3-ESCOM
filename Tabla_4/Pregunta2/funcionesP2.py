""" FUNCIONES DE LA TABLA 4, PREGUNTA 2 - REDES III """
import sys
import os
import telnetlib
import time
from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText

"""----- Función para mostrar la fecha de la última vez que se recolectaron los archivos de configuración ----"""
def mostrarUltimaSolicitud():
    archivo = open("bitacora.txt", "r+")
    contenido = archivo.read()
    print("\n La ultima vez que se recolectaron los archivos fue el: %s " % contenido)
    archivo.close()
""" ......................................................................................................"""

"""---- Función para mostrar una pregunta en pantalla y cpaturar la respuesta a esta pregunta ----"""
def mostrarPregunta():
    pregunta = "------>  Desea ingresar recolectar la informacion de los dispositivos ? <------ "
    instrucciones = " Si su respuesta es: SI , ingrese el numero 1 \n Si su repuesta es: NO, ingrese el numero 2"
    print(pregunta)
    print(instrucciones)
    respuesta = int(input(" Ingrese su respuesta: "))
    return respuesta
""" ......................................................................................................"""

""" ---- Función para terminar un programa en python ---- """
def terminarEjecucion():
    print(" .... Fin de la ejecucion .... ")
    sys.exit()
""" ......................................................................................................"""

""" ------------------ Función para extraer los archivos de configuración de los routers ------------------- """
def obtenerConfiguraciones():
    direcciones = ['10.1.200.1', '10.5.200.1', '10.7.200.1', '10.8.200.1', '10.9.200.1', '10.12.200.1', '10.11.200.2', '10.13.200.1', '10.14.200.1', '10.15.200.1']
    user = "humberto"
    password = "123456"
    copy = "copy running-config tftp"
    destino = "10.1.200.3"
    salir = "exit"

    for direccion in direcciones:
        tn = telnetlib.Telnet(direccion)
        tn.read_until(b"Username: ")
        tn.write(user.encode('ascii') + b"\n")
        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")
        tn.write(copy.encode('ascii') + b"\n")
        tn.write(destino.encode('ascii') + b"\n")
        tn.write(b"\n")
        time.sleep(1)
        tn.write(salir.encode('ascii') + b"\n")
        print(tn.read_all().decode('ascii'))
    
    print(" ----------> Archivos recolectados <---------- ")
    os.system("date +\'%d/%m/%Y  %H:%M:%S\'>bitacora.txt")
    bitacora = open("bitacora.txt", "r")
    contenido = bitacora.read()
    bitacora.close()
    print(" ¡¡¡ Nueva actualizacion !!! | Fecha: %s " % contenido)
    os.system("cp ../../../tftpboot/* configurciones/")
    os.system("ls configurciones/>status.txt")
    return contenido
""" ......................................................................................................"""

""" .......................... Función para enviar un WhatsApp .......................... """
def enviarWhats(fecha):
    account_sid = ''
    auth_token = ''
    cliente = Client(account_sid, auth_token)
    archivo = open("status.txt", "r")
    status = archivo.read()
    archivo.close()

    whats = " ¡ Archivos recolectados ! \n Fecha: %s \n Archivos: \n %s " % (fecha, status)

    mensaje = cliente.messages.create(
    body = whats,
    from_= 'whatsapp:+',
    to = 'whatsapp:+52155...'
    )
    time.sleep(1)
    print(" ¡ Notificación de WhatsApp enviada !")
""" ......................................................................................................"""

""" ..................... Función para enviar un correo electrónico ................ """
def enviarCorreo(fecha):
    archivo = open("status.txt", "r")
    status = archivo.read()
    archivo.close()

    from_addr = "@gmail.com"
    to_addr = ""

    mensaje = MIMEText("¡ Archivos recolectados ! \n Fecha: " + fecha + "\n Archivos: " + status)
    mensaje['From'] = from_addr
    mensaje['To'] = to_addr
    mensaje['Subject'] = "Archivos recolectados"

    username = ""
    password = ""

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(username, password)
    server.sendmail(from_addr, to_addr, mensaje.as_string())
    server.quit()
    print(" ¡ Notificación de correo enviada !")
""" ......................................................................................................"""
