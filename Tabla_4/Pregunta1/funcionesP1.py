""" FUNCIONES CREADAS PARA LA PREGUNTA 1 DE LA TABLA 4 - REDES III """
import telnetlib
from twilio.rest import Client
import time
import smtplib
from email.mime.text import MIMEText
""" .............. Función para extraer la información del HW de un router a través de telnet .............. """
def extraerInformacion(direccion):
    user = "humberto"
    password = "123456"
    show = "show version"
    salir = "exit"
    espacio = " "
    nombre_archivo = "buffer.txt"

    archivo = open(nombre_archivo, "w+")
    tn = telnetlib.Telnet(direccion)

    print(" ¡¡¡ CONEXIÓN TELNET EXITOSA !!! ")

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(show.encode('ascii') + b"\n")
    tn.write(espacio.encode('ascii') + b"\n")

    tn.write(salir.encode('ascii') + b"\n")

    archivo.write(tn.read_all().decode('ascii'))
    print(archivo.read())
    archivo.close()

    print (" ¡¡¡ FIN DE LA CONEXIÓN !!! ")
    return nombre_archivo
""" ..................................................................................... """
""" ......... Función para extraer el id del router .......... """
def extraerID(nombre_archivo):
    bandera = 0
    archivo = open(nombre_archivo, "r")
    while bandera != 1:
        cadena = archivo.readline()
        posicion = cadena.find("#")
        if posicion >= 0:
            bandera = 1
            cadena_final = cadena
    archivo.close()

    print ("P: %d " % posicion)
    print (cadena_final)
    hostname = cadena_final[0:posicion]
    print("Hostname: " + hostname)

    return hostname
""" ..................................................................................... """
""" ......... Función para extraer la información del HW del router .......... """
def extraerInformacionHardware(nombre_archivo, nombre_router):
    bandera = 0
    archivo = open(nombre_archivo, "r")

    while bandera != 1:
        cadena = archivo.readline()
        posicion = cadena.find("export@cisco.com.")
        if posicion >= 0:
            posicion = archivo.tell()
            bandera = 1

    print ("P: %d " % posicion)
    archivo.seek(posicion)
    contenido = archivo.read()
    archivo.close()

    tipo = type(contenido)
    print (tipo)
    print (contenido)

    limite = contenido.find("R1#")
    print("%d" % limite)

    salida = open(nombre_router, "w+")
    hardware = contenido[0:limite]

    salida.write(hardware)

    salida.close()

    return hardware
""" ..................................................................................... """
""" .......................... Función para enviar un WhatsApp .......................... """
def enviarWhats(router, ip, contenido):
    account_sid = ''
    auth_token = ''
    cliente = Client(account_sid, auth_token)

    whats = " ID: " + router + "\n IP: " + ip + "\n Información: " + contenido 

    mensaje = cliente.messages.create(
    body = whats,
    from_= 'whatsapp:+',
    to = 'whatsapp:+52155......'
    )
    time.sleep(1)
    print(" ¡ Notificación de WhatsApp enviada !")

""" ..................... Función para enviar un correo electrónico ................ """
def enviarCorreo(router, ip, contenido):
    from_addr = "@gmail.com"
    to_addr = "@gmail.com"

    mensaje = MIMEText("ID: %s \n IP: %s \n Información: %s " % (router, ip, contenido))
    mensaje['From'] = from_addr
    mensaje['To'] = to_addr
    mensaje['Subject'] = " Información de dispositivo"

    username = "@gmail.com"
    password = ""

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(username, password)
    server.sendmail(from_addr, to_addr, mensaje.as_string())
    server.quit()
    print(" ! Notificacion de correo enviada !")
""" ................................................................................................................... """
