import os  
import sys                         
import time
import shutil
from twilio.rest import Client

""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    La función obtenerIP() lee la lista de IPs del archivo: ips.txt y la muestra en pantalla con 
    un retardo de 1 segundo a través de la función sllep()
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
""" 
def obtenerIP():                
    archivo = open("ips.txt", "r")
    print (" ... OBTENIEDO IPs ... ")
    for c in range(0, 25):
        cadena = archivo.readline() 
        print (cadena) 
        time.sleep(1)
    print (" ... IPs obtenidas ... \n")

""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    La función realizarPING() lee la lista de direcciones IP del archivo: ips.txt y realiza un ping
    a cada IP a través de la función os.system(). Se realizan 4 iteraciones, es decir, 
    a cada IP de la lista de IP's se le realizan 4 PING en total.
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
def realizarPING():
    archivo2 = open("adverts.txt", "w")
    for i in range(1, 4):
        archivo = open("ips.txt", "r")
        print ("\n ************** Iteracion %d **************** " % (i))
        archivo2.write("************ ITERACION %d ************ \n" % (i))
        for c in range(0, 25):
            cadena = archivo.readline() 
            print (cadena) 
            comando = "ping -c 3 " + cadena
            output = os.system(comando)
            if output == 0:
                print (" ---------> SI RESPONDE <------------- \n ")
            else:
                print (" !!!!!!!!!!!!! NO REPONDE !!!!!!!!!!! \n")
                ip = cadena
                archivo2.write(" La ip " + ip + "no respondio \n")
                
        archivo.close()
    archivo2.close()
""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Al final de realizar los PING, las IP que no respondieron al PING se registran en un archivo de 
    texto llamado: adverts.txt . Al final del programa se lee el archivo adverts.txt y se imprime en 
    pantalla.
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
print (" - - - - - - - - - - - - - PING PULLER - - - - - - - - - - - - - \n")
account_sid = ''
auth_token = ''
cliente = Client(account_sid, auth_token)


obtenerIP()
realizarPING()
os.system("clear")
print(" \n ... RESULTADOS OBTENIDOS .... \n")
resultado = open("adverts.txt", "r")
contenido = resultado.read()
print (contenido)
correo = "echo \"" + contenido + "\" | mail -s \" PING PULLER !!! \" correo_electronico@gmail.com"
os.system(correo)

whatsapp = " PING PULLER !!! " + contenido
mensaje = cliente.messages.create(
    body = whatsapp,
    from_= 'whatsapp:+',
    to = 'whatsapp:+52155......'
)
