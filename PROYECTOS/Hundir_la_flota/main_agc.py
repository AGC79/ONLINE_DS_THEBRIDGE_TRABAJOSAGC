import PROYECTOS.Hundir_la_flota.funciones_agc as funciones_agc

tablero_vacio = funciones_agc.tablero()

tablero_jugador = funciones_agc.colocar_barcos(tablero_vacio)
print("\n\nTablero generado para el jugador:\n\n", tablero_jugador, "\n\n")

tablero_rival = funciones_agc.colocar_barcos(tablero_vacio)
print("Tablero generado para el rival:\n\n", tablero_jugador, "\n\n")
