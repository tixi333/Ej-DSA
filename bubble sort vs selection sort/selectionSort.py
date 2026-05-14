def selectionSort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]       
    
    return arr

arr = [73, 5, 91, 28, 64, 12, 100, 47, 3, 86]
selectionSort(arr)
print(arr)