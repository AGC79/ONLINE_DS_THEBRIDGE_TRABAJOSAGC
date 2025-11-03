from clase import Fichero

loc_fichero = Fichero()
print(loc_fichero.ruta_fichero)

loc_fichero.crear_carpetas_destino()

loc_fichero.mover_archivos()