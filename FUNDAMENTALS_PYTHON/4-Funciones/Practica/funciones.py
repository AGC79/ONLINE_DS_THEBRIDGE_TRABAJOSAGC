import math

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