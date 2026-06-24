import time
from listas import crear_lista

def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        
        numC = arr[i] #numero a comparar
        j = i - 1 # posicion del numero a la izquierda (numI)
        
        #mientras la posicion no sea menor a 0
        # y numc sea menor a numI

        while j >= 0 and numC < arr[j]:
            arr[j +1] = arr[j] #es menor asi que se mueve a la derecha
            j -= 1 #siguiente posicion a la izquierda
        
        # cuando numI sea menor o igual a numC
        # se coloca numC a la derecha de numI
        
        arr[j + 1] = numC
    
    return arr

def main(largo):
    total = []
    for i in largo:
        lista = crear_lista(i)
        print(lista)
        inicio = time.perf_counter()
        insertionSort(lista)
        fin = time.perf_counter()
        total.append(fin - inicio)
    return total
