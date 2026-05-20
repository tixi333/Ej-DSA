def insertionSort(arr):
    for i in range(1, len(arr)):
        numC = arr[i]
        j = i - 1
        while j >= 0 and numC < arr[j]:
            arr[j +1] = arr[j]
            j -= 1
        arr[j + 1] = numC
    
    return arr
        
        
arr = [73, 5, 91, 28, 64, 12, 100, 47, 3, 86]
print(insertionSort(arr))