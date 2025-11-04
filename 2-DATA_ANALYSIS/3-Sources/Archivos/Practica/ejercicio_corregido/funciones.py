import os
from variables import *
import shutil

#___________________________________________________________
def comp_archivos():
    for i in os.listdir(ruta_carpeta):

        if os.path.isdir(i):
            i = i.lower()
            print("Es una carpeta")
            continue
        elif i.endswith(doc_types):
            try:
                print(i, "es un documento")
                shutil.move(i, "Documentos")
            except:
                print("Ya está en la carpeta 'Documentos'")
        elif i.endswith(img_types):
            try:
                print(i, "es una imagen")
                shutil.move(i, "Imagenes")
            except:
                print("Ya está en la carpeta 'Imagenes'")
        elif i.endswith(software_types):
            try:
                print(i, "es un programa")
                shutil.move(i, "Software")
            except:
                print("Ya está en la carpeta 'Software'")
        else:
            try:
                print(i, "no es conocido")
                shutil.move(i, "Otros")
            except:
                print("Ya está en la carpeta 'Otros'")


def crear_carp():
    os.chdir(ruta_carpeta)
    os.makedirs("Documentos", exist_ok=True)
    os.makedirs("Imagenes", exist_ok=True)
    os.makedirs("Software", exist_ok=True)
    os.makedirs("Otros", exist_ok=True)