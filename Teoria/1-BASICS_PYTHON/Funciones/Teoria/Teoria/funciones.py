def multi_lista(n, *args):
    lista_ejemplo = []
    for lista in args:          
        for i in lista:
            lista_ejemplo.append(i * n)
    return lista_ejemplo       

def juntar_listas(lista_1, lista_2, lista_3):
    return lista_1 + lista_2 + lista_3