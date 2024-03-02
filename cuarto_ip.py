# cuarto_ip.py

import os
import sys

red = sys.argv[1] if len(sys.argv) > 1 else "10.13.123"
inicio = int(sys.argv[2]) if len(sys.argv) > 2 else 1
fin = int(sys.argv[3]) if len(sys.argv) > 3 else 10

for i in range(inicio,fin+1):
    ip = red + "." + str(i)
    response = os.system("ping -n 1 " + ip)
    if response == 0:
        print(ip + " Activo")
    else:
        print(ip + "Inactivo")
