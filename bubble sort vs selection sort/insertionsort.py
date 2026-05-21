def insertionSort(arr):
    for i in range(1, len(arr)):
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
        
        
arr = [73, 5, 91, 28, 64, 12, 100, 47, 3, 86]
print(insertionSort(arr))