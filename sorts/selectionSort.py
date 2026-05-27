import time
from listas import crear_lista

def selectionSort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    
    return arr

def main(largo):
    total = []
    for i in largo:
        lista = crear_lista(i)
        print(lista)
        inicio = time.perf_counter()
        selectionSort(lista)
        fin = time.perf_counter()
        total.append(fin - inicio)
    return total