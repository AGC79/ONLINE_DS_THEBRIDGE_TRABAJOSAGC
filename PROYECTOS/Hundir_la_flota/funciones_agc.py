import numpy as np
import random
<<<<<<< HEAD
import time

### MÉTODO PARA CREAR TABLERO VACIO
=======

### CREACIÓN DE TABLERO VACIO
>>>>>>> 310164a296ff92d7f713460f6cd7d4e4b3bbfce5
def tablero():
    tablero = np.full((10,10), "_")
    return tablero

<<<<<<< HEAD
### MÉTODO PARA DISPARAR
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

=======
>>>>>>> 310164a296ff92d7f713460f6cd7d4e4b3bbfce5
### MÉTODO PARA COLOCAR BARCOS DE MANERA ALEATORIA EN TABLERO VACIO
def colocar_barcos(tablero):

    barcos_plantilla = [
        [[0,0], [0,0]], 
        [[0,0], [0,0]], 
        [[0,0], [0,0]], 
        [[0,0], [0,0], [0,0]], 
        [[0,0], [0,0], [0,0]], 
        [[0,0], [0,0], [0,0], [0,0]]
    ]

    for i in range(len(barcos_plantilla)): # i es el indice de cada barco iterado
        eslora = len(barcos_plantilla[i])
        orientacion = random.choice(["N", "S", "E", "W"])
        
        while True:

            # Lista para guardar coordenadas. Si hay solapamiento, se reinicia el while y se vuelve a generar otra
            barcos_jugador = []

            # Límites en la matriz para colocar la primera casilla de los barcos. Se establecen a la hora de generar las coordenadas aleatorias
            if orientacion == "N":
                # eslora -1, es la casilla inicial hacia arriba, contando desde la posición 0 hacia abajo
                fila = random.randint(eslora - 1, 9)
                columna = random.randint(0, 9)
            elif orientacion == "S":
                # 10 - eslora, es la casilla inicial hacia abajo, contando desde la posición 0 hacia abajo
                fila = random.randint(0, 10 - eslora)
                columna = random.randint(0, 9)
                # 10 - eslora, es la casilla inicial hacia la derecha, contando desde la posicion 0 hacia la izquierda
            elif orientacion == "E":
                fila = random.randint(0, 9)
                columna = random.randint(0, 10 - eslora)
            else:  # W
                # eslora - 1, es la casilla inicial hacia la izquierda, contando desde la posicion 0 hacia la izquierda
                fila = random.randint(0, 9)
                columna = random.randint(eslora - 1, 9)
            
            barcos_jugador.append([fila, columna])
            
            # Resto de casillas según la orientación
            # j es el elemento de la eslora iterado
            # el elemento de la posición 0 de la eslora de los barcos ya se ha asignado, la iteración se realiza sobre el rango entre el elemento 1 de la eslora de cada barco
            # i longitud de la eslora (sin contar el ultimo numero)
            for j in range(1, eslora): 
                if orientacion == "N":
                    fila_o = fila - j # [2,5][1,5][0,5]
                    columna_o = columna
                elif orientacion == "S":
                    fila_o = fila + j
                    columna_o = columna
                elif orientacion == "E":
                    fila_o = fila
                    columna_o = columna + j
                else:  # "O"
                    fila_o = fila
                    columna_o = columna - j
                barcos_jugador.append([fila_o, columna_o])

            # print(barcos_jugador)
            solapamiento = False
            for fila, columna in barcos_jugador:
                if tablero[fila, columna] == "O":
                    solapamiento= True # Como se encuentra solapamiento, se sale del bucle for y se comienza de nuevo el while
                    break 
            if not solapamiento:
                for fila, columna in barcos_jugador:
                    tablero[fila, columna] = "O"
                break # si no hay solapamiento, se ponen los barcos y se sale del bucle while
    return tablero