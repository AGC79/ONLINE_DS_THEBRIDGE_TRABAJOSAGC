import os
import shutil

script_path = os.path.dirname(os.path.abspath('__file__'))
print("ruta script", script_path)
os.chdir(os.path.join(script_path, "descargas_agc")) # descargas_agc esta en la mismma carpeta desde en la que se encuentra el script de python
print("Ruta absoluta del directorio que se quiere ordenar:\n", os.getcwd())

lista_carpetas = ["Imagenes", "Documentos", "Software", "Otros"]
# print(serie_carpetas)

doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
software_types = ('.exe', '.py','.ipynb')

for dir in lista_carpetas:
    os.makedirs(dir, exist_ok=True)
    #if dir not in os.listdir():
        #os.mkdir(dir)

for file in os.listdir():

    if os.path.isdir(file):
        continue

    movido = False # bandera
    
    for i in doc_types:
        if file.endswith(i):
            # print(file)
            try:
                shutil.move(file, "Documentos")
                print(f"Movido archivo {file} al directorio 'Documentos'")
            except Exception as e: 
                print(e)
                print(f"Este archivo ya existe en la carpeta Documentos.\n Se omite la operación.")
            movido = True
            break
    if not movido:
        for j in img_types:
            if file.endswith(j):
                # print(file)
                try:
                    shutil.move(file, "Imagenes")
                    print(f"Movido archivo {file} al directorio 'Imagenes'")
                except Exception as e: 
                    print(e)
                    print(f"Este archivo ya existe en la carpeta Imagenes.\n Se omite la operación.")
                movido = True
                break
    if not movido:
        for x in software_types:
            if file.endswith(x):
                #print(file)
                try:
                    shutil.move(file, "Software")
                    print(f"Movido archivo {file} al directorio 'Software'")
                except Exception as e:
                    print(e)
                    print(f"Este archivo ya existe en la carpeta Software.\n Se omite la operación.")
                movido = True
                break
    if not movido:
        try:
            shutil.move(file, "Otros")
            print(f"Movido archivo {file} al directorio 'Otros'")
        except Exception as e:
            print(e)
            print(f"Este archivo ya existe en la carpeta Otros.\n Se omite la operación.")


