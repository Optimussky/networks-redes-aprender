# rename_pdf.py

import os
import re

def renombrar_archivos():
    directorio = os.getcwd() # obtener directorio actual
    archivos_pdf = [archivo for archivo in os.listdir(directorio) if archivo.endswith(".pdf")]

    for archivo in archivos_pdf:
        nuevo_nombre = re.sub(r"\s", "-",archivo) # Reemplazar espacios por -
        ruta_vieja = os.path.join(directorio,archivo)
        ruta_nueva = os.path.join(directorio,nuevo_nombre)
        os.rename(ruta_vieja, ruta_nueva)

    print("Archivos renombrados con éxito.")

if __name__ == "__main__":
    renombrar_archivos()
