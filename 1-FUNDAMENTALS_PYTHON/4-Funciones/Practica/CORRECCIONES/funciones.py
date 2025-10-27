# IMPORTS
import math
import numpy
#FUNCIONES 

def dias(dia):
    match dia:
        case 1:
            nombre_dia = "Lunes"
        case 2:
            nombre_dia = "Martes"
        case 3:
            nombre_dia = "Miercoles"
        case 4:
            nombre_dia = "Jueves"
        case 5:
            nombre_dia = "Viernes"
        case 6:
            nombre_dia = "Sabado"
        case 7:
            nombre_dia = "Domingo"
        case _:
            nombre_dia = "Dia no valido"

    return nombre_dia

def piramide(n):
    lista = list(range(n, 0, -1))
    while len(lista) > 0:
        print(*lista)
        lista.pop(0)
   
def comp(n_1, n_2):
    if n_1 == n_2:
        res = "Los numeros son iguales"
    elif n_1 > n_2:
        res = "El primer numero es mayor que el segundo."
    else:
        res = "El segundo numero es mayor que el primero"
    
    return res

def contar(texto, letra):
    try:
        texto = texto.lower()
        letra = letra.lower()
        return texto.count(letra)
    except:
        return "Valor no correcto"
    
def cont_letras(texto):
    texto = texto.lower()
    dict_letras = {}

    for i in texto:
        if i.isalpha():
            if i in dict_letras:
                dict_letras[i] += 1
            else:
                dict_letras[i] = 1
    return dict_letras

def add_lista(lista, comando, elemento = None): 
    comando = comando.lower()
    if comando == "add" and elemento is not None:
        lista.append(elemento)
    elif comando == "remove":
        try:
            lista.remove(elemento) 
        except:
            return "Elemento no encontrado en la lista"
    else:
        return "Comando incorrecto"
    return lista

def palabras(*args):
    return " ".join(args)

def cuadrado(l):
    return l**2

def triangulo(b, a):
    return b*a/2

def circulo(r):
    return math.pi * r**2