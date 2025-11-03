from clase import Fichero

# Instancia de la clase Fichero con la ruta de la carpeta descargas que se desea limpiar
loc_fichero = Fichero()
print(loc_fichero.ruta_fichero)

# Llamada a función que crea los directorios a donde deben moverse los archivos según su extensión
loc_fichero.crear_carpetas_destino()

# Llamada a función que mueve los ficheros a su directorio correspindiente segun su extensión
loc_fichero.mover_archivos()