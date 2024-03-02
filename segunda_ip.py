# segunda_ip.py

"""
Programa que escanea las IP(equipos) que están en X segmento de red
para ejecutar este programa, escribir desde terminal en windows:
    python segunda_ip.py 10.13.123 | FINDSTR "Activo"

En linux:
    python segunda_ip.py 10.13.123 | grep Activo
"""
import os
import sys

red = sys.argv[1]# if leng(sys.argv) > 1 else "10.13.123"

if red == "":
    red = "10.13.123"

for i in range(40,49):
    ip = red + "." + str(i)
    response = os.system("ping -n 1 " + ip)
    if response == 0:
        print(ip + " Activo")
    else:
        print(ip + " Inactivo")
