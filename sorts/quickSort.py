import time
from listas import crear_lista

def partition(array, low, high):
    pivot = array[high] # elegir pivot (ultimo en este caso)

    i = low - 1 #indice - posicion final del pivot
    for j in range(low, high): # recorre la lista
        if array[j] <= pivot:
            #aumenta el indice si es menor (x lo tanto no se hace el swap)
            i += 1
            array[i], array[j] = array[j], array[i]
    
    #si el pivot es menor al valor se intercambian
    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1
        
    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1) # primera "mitad"
        quicksort(array, pivot_index+1, high) # segunda "mitad"

def main(largo):
    total = []
    for i in largo:
        lista = crear_lista(i)
        print(lista)
        inicio = time.perf_counter()
        quicksort(lista)
        fin = time.perf_counter()
        total.append(fin - inicio)
    return total