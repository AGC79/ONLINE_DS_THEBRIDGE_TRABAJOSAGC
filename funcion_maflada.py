def sacar_media(array):
    suma = 0

    for fila in array:
        #print(fila)
        for num in fila:
            # print(num)
            suma = suma + num
    print("Suma de todos los numeros:", suma)
    media_numeros = suma / 25
    # print(media_numeros)
    return media_numeros