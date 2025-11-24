from modelo_1 import lm

v1 = float(input("Datos de la casa:"))
v2 = float(input("Datos de la casa:"))
v3 = float(input("Datos de la casa:"))
v4 = float(input("Datos de la casa:"))
v5 = float(input("Datos de la casa:"))

lista = [[v1, v2, v3, v4, v5]]

pred_input = lm.predict(lista)
# [[12,12,12,12,12]]
print("Tu casa vale: ", pred_input[0], "€")