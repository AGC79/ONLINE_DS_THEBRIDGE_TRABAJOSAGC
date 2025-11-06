from funciones import *

print("Abriendo navegador con Python...")

navegador = acceso_pag()

pulsar_aceptar(navegador)

print("Accediendo a la pagina para hacer web scraping...")

print("Extrayendo listado de películas...")

lista_peliculas_top = extraer_peliculas_top(navegador)

convertir_csv(lista_peliculas_top)

print("Listado de películas converdido a formato csv...")

cerrar_nav(navegador)

print("Navegador cerrado.")