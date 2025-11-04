import os
import spotipy 
import pandas as pd

from spotipy.oauth2 import SpotifyOAuth

def borrar_cache():
    if os.path.exists(".cache"):
        os.remove(".cache")

def autenticarse(nombre_artista, c_id, c_secret, uri):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id = c_id,
        client_secret = c_secret,
        redirect_uri = uri
    ))

    resultado_artista = sp.search(q = f'artist:{nombre_artista}', type='artist', limit=1)
    dict_artista = resultado_artista["artists"]["items"][0]
    print("Nombre:", dict_artista["name"])
    print("ID:", dict_artista["id"])

    id_artista = dict_artista["id"]
    
    return sp, id_artista

def obtener_albumes(sp, id_art):
    pag_actual_albumes = sp.artist_albums(id_art, limit=50)

    lista_dict_albumes = []

    lista_dict_albumes.extend(pag_actual_albumes["items"])

    while pag_actual_albumes["next"]:
        pag_actual_albumes = sp.next(pag_actual_albumes)
        lista_dict_albumes.extend(pag_actual_albumes["items"])

    return lista_dict_albumes

def obtener_tracks(sp, list_dict_alb):
    lista_tracks = []

    for album in list_dict_alb:
        album_id = album["id"] 
        album_name = album["name"]

        all_tracks = sp.album_tracks(album_id, limit = 50)

        while all_tracks["next"]:
            for track in all_tracks["items"]:
                lista_tracks.append({
                    "canción": track["name"],
                    "álbum": album_name
                })
            all_tracks = sp.next(all_tracks)

        for track in all_tracks["items"]:
            lista_tracks.append({
                "canción": track["name"],
                "álbum": album_name
            })

    return lista_tracks
            
def convertir_lista_df(ls_tracks):
    df_tracks_artista = pd.DataFrame(ls_tracks)
    print(df_tracks_artista)
    return df_tracks_artista

def convertir_df_dataset(df_artista):
    df_artista.to_csv("canciones_bob_marley.csv", sep = ';', index = True)
    df_artista.to_excel('canciones_bob_marley.xlsx')