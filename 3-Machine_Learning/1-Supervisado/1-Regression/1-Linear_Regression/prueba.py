from modelo import lm

v1 = float(input("Datos d la casa. Ingresos: "))
v2 = float(input("Datos d la casa. Años de antigüedad: "))
v3 = float(input("Datos d la casa. Salas: "))
v4 = float(input("Datos d la casa. Habitaciones: "))
v5 = float(input("Datos d la casa. Población: "))

lista = [[v1, v2, v3, v4, v5]]

pred_input = lm.predict(lista)

# [[12, 12, 12, 12, 12]]

print("Tu casa vale: ", pred_input)