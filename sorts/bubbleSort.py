import time
from listas import crear_lista

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

def main(largo):
    total = []
    for i in largo:
        lista = crear_lista(i)
        print(lista)
        inicio = time.perf_counter()
        bubble_sort(lista)
        fin = time.perf_counter()
        total.append(fin - inicio)
    return total
