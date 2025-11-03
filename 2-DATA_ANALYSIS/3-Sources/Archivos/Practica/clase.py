import os
import shutil

class Fichero:
    '''
    Clase que organiza archivos dentro de una carpeta específica ("descargas_agc"),
    moviéndolos a subcarpetas según su tipo (documentos, imágenes, software u otros).
    No recibe parámetros al instanciarse.
    '''

    def __init__(self):
        '''
        Constructor de la clase Fichero.

        Atributos:
            ruta_fichero (str): Ruta absoluta de la carpeta "descargas_agc", que debe estar en el mismo
                                directorio donde se ejecuta el script principal.
            lista_carpetas (list): Lista con los nombres de las carpetas de destino para clasificar los archivos.
            doc_types (tuple): Extensiones de archivos consideradas como documentos.
            img_types (tuple): Extensiones de archivos consideradas como imágenes.
            software_types (tuple): Extensiones de archivos consideradas como software o scripts.
        '''
        self.ruta_fichero = os.path.join(os.getcwd(), "descargas_agc")
        

        self.lista_carpetas = ["Imagenes", "Documentos", "Software", "Otros"]
        

        self.doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
        self.img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
        self.software_types = ('.exe', '.py', '.ipynb')


    def crear_carpetas_destino(self):
        '''
        Crea las carpetas de destino necesarias dentro de la ruta "descargas_agc".

        Inputs:
            No recibe parámetros externos. Usa el atributo "interno self.lista_carpetas".

        Outputs:
            None
        '''
        os.chdir(self.ruta_fichero)
        for dir in self.lista_carpetas:
            os.makedirs(dir, exist_ok=True)

    def mover_archivos(self):
        '''
        Mueve los archivos de la carpeta "descargas_agc" a su carpeta correspondiente
        según su extensión.

        Inputs:
            No recibe parámetros externos. 
            Usa los atributos internos "self.doc_types", "self.img_types" y "self.software_types".

        Outputs:
            None
        '''
        for file in os.listdir():

            if os.path.isdir(file):
                continue

            movido = False # bandera
        
            for i in self.doc_types:
                if file.endswith(i):
                    # print(file)
                    try:
                        shutil.move(file, "Documentos")
                    except Exception as e: 
                        print(e)
                        print(f"Este archivo ya existe en la carpeta Documentos.\n Se omite la operación.")
                    movido = True
                    break
            if not movido:
                for j in self.img_types:
                    if file.endswith(j):
                        # print(file)
                        try:
                            shutil.move(file, "Imagenes")
                        except Exception as e: 
                            print(e)
                            print(f"Este archivo ya existe en la carpeta Imagenes.\n Se omite la operación.")
                        movido = True
                        break
            if not movido:
                for x in self.software_types:
                    if file.endswith(x):
                        #print(file)
                        try:
                            shutil.move(file, "Software")
                        except Exception as e:
                            print(e)
                            print(f"Este archivo ya existe en la carpeta Software.\n Se omite la operación.")
                        movido = True
                        break
            if not movido:
                try:
                    shutil.move(file, "Otros")
                except Exception as e:
                    print(e)
                    print(f"Este archivo ya existe en la carpeta Otros.\n Se omite la operación.")