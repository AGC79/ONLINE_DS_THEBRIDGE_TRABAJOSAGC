def calcular_precio(distrito, superficie):
    if (distrito == "Moncloa" or distrito == "Centro") and superficie > 100:
        precio = 1000
        # print("El precio de la casa es", precio)
    elif distrito == "Salamanca" and superficie >= 150:
        precio = 1500
        # print("El precio de la casa es", precio)
    elif distrito != "Retiro" and (superficie >= 60 and superficie <= 80):
    # elif distrito != "Retiro" and 60 <= superficie <= 80:
        precio = 600
        #print("El precio de la casa es", precio)
    else:
        precio = 0
        #print("El precio de la casa es", precio)

    return f'El precio de la casa es {precio} euros'