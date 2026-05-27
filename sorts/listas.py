from random import randint

def crear_lista(n):
    lista = []
    for i in range(n):
        lista.append(randint(1,50))
    return lista