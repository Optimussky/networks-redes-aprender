# escaneo_rango_ip.py

import os

red = ""
red = input("Introduzca una red (por ejemplo 192.168.1): ")
#if red == "":
#    red = "10.13.123"
#red = ""
if red == "":
    red = "10.13.123"

for i in range(40,49):
    ip = red + "." + str(i)
    print(i)
    print("Ganando tiempo...")
    response = os.system("ping -n 1" + ip)
    if response == 0:
        print(ip + " está activa")
#    else:
#        print(ip + " no está activa")

