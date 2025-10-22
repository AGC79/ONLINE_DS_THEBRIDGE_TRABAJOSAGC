import numpy as np

def tablero():
    tablero = np.full((10,10), "_")
    return tablero

def colocar_tablero(tablero, lista):
    for barco in lista:
        print(barco)
        for posicion in barco:
            print(posicion)
            tablero[posicion] = "O"
    return tablero

def disparar(tablero, fila, columna):
    if tablero[fila, columna] == "O":
        print("Tocado")
        tablero[fila, columna] = "X"
    elif tablero[fila, columna == "#"]:
        disparar(tablero, fila, columna)
    else:
        print("Agua")
        tablero[fila, columna] = "#"
    return tablero