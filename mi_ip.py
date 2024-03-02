import os

red = input("Introduzca una red (por ejemplo 192.168.1): ")
if red == "":
    red = "192.168.1"

for i in range(1, 11):
    ip = red + "." + str(i)
    response = os.system("ping -n 1 " + ip)
    if response == 0:
        print(ip + " está activa")
    else:
        print(ip + " no está activa")
