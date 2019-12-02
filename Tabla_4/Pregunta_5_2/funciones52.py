""" FUNCIONES DE LA TABLA 4, PREGUNTA 2 - REDES III """
import sys
import os
import telnetlib
import time
from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText

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
    
    os.system("cp ../../../tftpboot/* configuraciones/")
""" ......................................................................................................"""
""" ------------------ Función para obtener el ID de un template a partir de un archivo de configuración ............ """
def obtenerID(configuracion):
    posicion = int(configuracion.find("-"))
    id_nombre = configuracion[0:posicion]
    return id_nombre
""" ......................................................................................................"""

""" .................. Función para extraer el comando de alguna línea del template ...................... """
def obtenerComando(linea):
    posicion = linea.find("$")
    posicion = posicion - 1                                                         # Para quitar el espacio
    comando = linea[0:posicion]
    return comando

""" ......................................................................................................"""

""" .................. Función para extraer una línea de la configuración a partir de un comando ...................... """
def obtenerLineaConfig(comando, nombre_archivo):
    archivo = open("configuraciones/" + nombre_archivo, "r")
    numero_lineas = len(archivo.readlines())
    archivo.seek(0)
    limite = 0
    while limite != numero_lineas:
        linea = archivo.readline()
        bandera = linea.find(comando)
        if bandera >= 0:
            archivo.close()
            return linea
        else:
            limite = limite + 1
    archivo.close()

""" ......................................................................................................"""

""" .................. Función para obtener el valor de una línea de configuración ....................... """
def obtenerValorConfig(linea):
    tamanio = len(linea)
    inicio = linea.find(" ")
    valor = linea[inicio + 1:tamanio - 1]
    return valor

""" ......................................................................................................"""

""" .................. Función para comparar los templates vs las configuraciones ........................ """
def compararArchivos():

    configuraciones = os.listdir("configuraciones")

    for configuracion in configuraciones:
        id_nombre = obtenerID(configuracion)
        id_template = "templates/" + id_nombre +"-template"
        print (id_template)
        template = open(id_template, "r+")
        numero_lineas = len(template.readlines())
        template.seek(0)
        iteraciones = 0
        lista = []
        while iteraciones != numero_lineas:
            linea = template.readline()
            comando = obtenerComando(linea)
            lista.insert(iteraciones, comando)
            iteraciones = iteraciones + 1
        template.close()
        print(lista)
        tamanio_lista = len(lista)

        linea_de_configuracion = obtenerLineaConfig(lista[0], configuracion) 
        print (linea_de_configuracion)
        valor_configuracion = obtenerValorConfig(linea_de_configuracion)
        print (valor_configuracion)
""" ......................................................................................................"""

""" ......................... Función para limpiar un template .......................................... """
def limpiarTemplates():
    templates = os.listdir("templates/")
    for template in templates:
        entrada = open("templates/" + template, "r")
        salida = open("tratamientoTemplates/" + template, "w+")
        lineas_entrada = len(entrada.readlines())
        entrada.seek(0)
        bandera = 0
        while bandera != lineas_entrada:
            linea = entrada.readline()
            linea = linea.replace("$", "")
            linea = linea.replace("{", "")
            linea = linea.replace("}", "")
            salida.write(linea)
            #print(linea)
            bandera =  bandera + 1
    salida.close()
    entrada.close()
    print("------> Tratamiento a templates concluido <-------")
""" ......................................................................................................"""

""" ................... Función para extraer pre-template de un archivo de configuración ................... """
def generarTemplateConfig():
    configuraciones = os.listdir("configuraciones/")
    for configuracion in configuraciones:
        entrada = open("configuraciones/" + configuracion, "r")
        salida = open("tratamientoConfigs/" + configuracion, "w+")
        lineas = len(entrada.readlines())
        entrada.seek(0)
        #print ("%d" % lineas)
        bandera = 0
        while bandera != lineas:
            linea = entrada.readline()
            if linea.find("hostname") >= 0:
                salida.write(linea)
                print(linea)
            if linea.find("username") >= 0:
                salida.write(linea)
                print(linea)
            if linea.find("interface") >= 0:
                nombre_i = linea
                ip = entrada.readline()
                if ip.find("no ip address") < 0:
                    nombre_i = nombre_i.replace("\n" , "")
                    nueva_linea = nombre_i + ip
                    salida.write(nueva_linea)
                    print(nueva_linea)
            if linea.find("router ospf") >= 0:
                salida.write(linea)
                print(linea)
            if linea.find("network") >= 0:
                salida.write(linea)
                print(linea)
            if linea.find("logging trap") >= 0:
                salida.write(linea)
                print(linea)
            if linea.find("logging") >= 0 and linea.find("logging trap") < 0 and linea.find("logging synchronous") < 0:
                salida.write(linea)
                print(linea)
            bandera =  bandera + 1
    entrada.close()
    salida.close()
    print("--------> Tratamiento a los archivos de configuracion terminado <---------")
""" ......................................................................................................"""

""" ........................... Función para construir un template .......................... """
def comparacionTemplates():
    templates = os.listdir("tratamientoConfigs/")
    for template in templates:
        nombre_salida = obtenerID(template)
        entrada = open("tratamientoConfigs/" + template, "r")
        salida = open("tratamientoFinal/" + nombre_salida + "-template", "w+")
        lineas = len(entrada.readlines())
        entrada.seek(0)
        bandera = 0
        while bandera != lineas:
            linea = entrada.readline()
            if linea.find("hostname") >= 0:
                tamanio = len(linea)
                inicio = linea.find("hostname")
                espacio = linea.find(" ")
                primera = linea[inicio:espacio + 1]
                segunda = linea[espacio + 1:tamanio - 1]
                temp = primera + "${" + segunda + "}\n"
                #print(temp)
                salida.write(temp)
            if linea.find("router ospf") >= 0:
                tamanio = len(linea)
                inicio = linea.find("router ospf")
                espacio = len("router ospf")
                primera = linea[inicio:espacio + 1]
                segunda = linea[espacio + 1:tamanio - 1]
                temp = primera + "${" + segunda + "}\n"
                #print(temp)
                salida.write(temp)
            if linea.find("logging trap") >= 0:
                tamanio = len(linea)
                inicio = linea.find("logging trap")
                espacio = len("logging trap")
                primera = linea[inicio:espacio + 1]
                segunda = linea[espacio + 1:tamanio - 1]
                temp = primera + "${" + segunda + "}\n"
                #print(temp)
                salida.write(temp)
            if linea.find("logging") >= 0 and linea.find("logging trap") < 0:
                tamanio = len(linea)
                inicio = linea.find("logging")
                espacio = linea.find(" ")
                primera = linea[inicio:espacio + 1]
                segunda = linea[espacio + 1:tamanio - 1]
                temp = primera + "${" + segunda + "}\n"
                #print(temp)
                salida.write(temp)
            if linea.find("interface") >= 0:
                lista = list(linea.split(" "))
                ultimo = lista[5]
                ultimo = ultimo.replace("\n", "")
                temp = lista[0] + " ${" + lista[1] + "} " + lista[2] + " " + lista[3] + " ${" + lista[4] + "} ${" + ultimo + "}\n" 
                #print(temp)
                salida.write(temp)
            if linea.find("network") >= 0:
                lista = list(linea.split(" "))
                ultimo = lista[5]
                ultimo = ultimo.replace("\n", "")
                temp = lista[1] + " ${" + lista[2] + "} ${" + lista[3] + "} " + lista[4] + " ${" + ultimo + "}\n"
                #print(temp)
                salida.write(temp)
            bandera = bandera + 1
        salida.seek(0)
        contenido = salida.read()
        enviarCorreo(contenido)
        enviarMensaje(contenido)
    entrada.close()    
    salida.close()
    print("-----------------> TEMPLATES ACTUALIZADOS <----------------")
    os.system("cp tratamientoFinal/* templates/")
""" ......................................................................................................"""

""" ........................... Función para enviar un correo electrónico ............................... """
def enviarCorreo(contenido):

    from_addr = ""
    to_addr = ""

    mensaje = MIMEText("¡ Template actualizado ! \n " + contenido)
    mensaje['From'] = from_addr
    mensaje['To'] = to_addr
    mensaje['Subject'] = "¡ Template actualizado !"

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

def enviarMensaje(contenido):
    account_sid = ''
    auth_token = ''

    whatsapp = " ¡ TEMPLATE ACTUALZIADO ! \n" + contenido
    cliente = Client(account_sid, auth_token)
    mensaje = cliente.messages.create(
        body = whatsapp,
        from_= 'whatsapp:+',
        to = 'whatsapp:+52155...'
    )
    print(" ¡ Notificación de WhatsApp enviada !")
""" ..................................................................................... """
