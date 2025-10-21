# IMPORTS
import math

# FUNCIONES



def convertir_numero_semana(num:int):

    lista_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for num_semana, dia in enumerate(lista_dias):
        if num == num_semana + 1:
            return dia
    if num <= 0 or num > 7:
       return "Número de día incorrecto"
    
def crear_piramide(filas:int):
    
    for i in range(filas, 0, -1): 
        for j in range(i, 0, -1):  
            print(j, end=" ")       
        print()  


def comparar_numeros(num_01, num_02):
    if num_01 == num_02:
        return f"Los dos numeros introducidos son iguales."
    elif num_01 > num_02:
        return f"El número {num_01} es mayor que el número {num_02}."
    else:
        return f"El número {num_02} es mayor que el número {num_01}."

def contar_letras(texto:str, letra:str):

    contador = 0

    for i in range(len(texto)):
        if letra.lower() == texto[i].lower():
            contador += 1

    return f"Veces que se repite la letra \"{letra}\" en el texto introducido: {contador}."

def crear_diccionario(texto2:str):

    dict_letras = {}
    for letra in texto2.lower(): 
        if letra not in dict_letras:
            dict_letras[letra] = 1
        else:
            dict_letras[letra] = dict_letras[letra] + 1

    return dict_letras

def crear_diccionario2(texto2:str):

    dict_letras = {}
    for letra in texto2.lower(): 
        if letra.isalpha():
            if letra not in dict_letras:
                dict_letras[letra] = 1
            else:
                dict_letras[letra] = dict_letras[letra] + 1

    return dict_letras

def modificar_lista(lista, comando:str, elemento=None):
    if comando == "add":
        lista.append(elemento)
    elif comando == "remove":
        if elemento in lista:
            lista.remove(elemento)
    else:
        print("Este comando no funciona, introduce \"add\" o \"remove\".")
    return lista

def crear_frase(*palabras):
    return " ".join(palabras)

def serie_fibonacci(numero:int):
    if numero <= 0:
        return 0  
    elif numero == 1:
        return 1
    else:
        return serie_fibonacci(numero - 1) + serie_fibonacci(numero - 2)
    
def calcular_area_cuadrado(lado):
    area_cuadrado = lado ** 2
    return area_cuadrado 

def calcular_area_triangulo(base, altura):
    area_triangulo = (base * altura) / 2
    return area_triangulo 

def calcular_area_circulo(radio):
    PI = round(math.pi, 2)
    area_circulo = PI * (radio ** 2)
    return area_circulo 