import os

# HABILITAR LA TAP0
comando1 = "ifconfig tap0 up"
os.system( comando1 )
print(" tap0 habilitada ... \n ")

# CONFIGURAR LA IP DE LA TARJETA ETHERNET: enp3s0f1
comando2 = "ifconfig enp3s0f1 10.1.200.3 netmask 255.255.255.0"
os.system( comando2 )
print(" enp3s0f1 configurada ... \n ")

# CONFIGRAR LA IP DE LA TAP0 
comando3 = "ifconfig tap0 10.1.200.2 netmask 255.255.255.0"
os.system( comando3 )
print(" tap0 configurada ... \n ")

# ELIMINAR LA INTERFAZ ETHERNET DE LA TABLA ruoute
comando4 = "route del -net 10.1.200.0 netmask 255.255.255.0 dev enp3s0f1"
os.system( comando4 )
print(" enp3s0f1 eliminada de la tabla de ruteo ... \n ")
# - - - - - - - - - - - - - - - - - RUTEO ESTÁTICO - - - - - - - - - - - - - - - - - - -
comando5 = "route add -net 10.2.200.0 netmask 255.255.255.252 gw 10.1.200.1 dev tap0"
comando6 = "route add -net 10.3.200.0 netmask 255.255.255.252 gw 10.1.200.1 dev tap0"
comando7 = "route add -net 10.4.200.0 netmask 255.255.255.252 gw 10.1.200.1 dev tap0"
comando8 = "route add -net 10.5.200.0 netmask 255.255.255.252 gw 10.1.200.1 dev tap0"
comando9 = "route add -net 10.6.200.0 netmask 255.255.255.252 gw 10.1.200.1 dev tap0"
comando10 = "route add -net 10.7.200.0 netmask 255.255.255.252 gw 10.1.200.1 dev tap0"
comando11 = "route add -net 10.8.200.0 netmask 255.255.255.252 gw 10.1.200.1 dev tap0"
comando12 = "route add -net 10.9.200.0 netmask 255.255.255.252 gw 10.1.200.1 dev tap0"
comando13 = "route add -net 10.10.200.0 netmask 255.255.255.252 gw 10.1.200.1 dev tap0"
comando14 = "route add -net 10.11.200.0 netmask 255.255.255.252 gw 10.1.200.1 dev tap0"
comando15 = "route add -net 10.12.200.0 netmask 255.255.255.252 gw 10.1.200.1 dev tap0"
comando16 = "route add -net 10.13.200.0 netmask 255.255.255.252 gw 10.1.200.1 dev tap0"
comando17 = "route add -net 10.14.200.0 netmask 255.255.255.252 gw 10.1.200.1 dev tap0"
comando18 = "route add -net 10.15.200.0 netmask 255.255.255.252 gw 10.1.200.1 dev tap0"

os.system(comando5)
os.system(comando6)
os.system(comando7)
os.system(comando8)
os.system(comando9)
os.system(comando10)
os.system(comando11)
os.system(comando12)
os.system(comando13)
os.system(comando14)
os.system(comando15)
os.system(comando16)
os.system(comando17)
os.system(comando18)