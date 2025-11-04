from funciones import *

borrar_cache()

sp, id_artista = autenticarse("Bob Marley", 
                              "meter aqui client_id de spotify", 
                              "meter aqui client_secret de spotify",
                              "meter aqui uri de spotify")

lista_albumes= obtener_albumes(sp, id_artista)

print("Obteniendo  todas las canciones del artista...")

lista_tracks = obtener_tracks(sp, lista_albumes)

df_artista = convertir_lista_df(lista_tracks)

convertir_df_dataset(df_artista)

print("Exportados datos en formato csv y Excel")