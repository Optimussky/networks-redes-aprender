
"""
Programa que escanea los equipos en red en determinado segmento.
Se puede ejecutar en terminal este programa, escribiendo:
    py tercera_ip.py 10.13.123|grep Activo|msg *
"""
import os
import sys
red = sys.argv[1] if len(sys.argv) > 1 else "10.13.123"
inicio = sys.argv[2]
fin = sys.argv[3]
for i in range(inicio, fin):
    ip = red + "." + str(i)
    response = os.system("ping -n 1 " + ip)
    if response == 0:
        print(ip + " Activo")
    else:
        print(ip + " Inactivo")
