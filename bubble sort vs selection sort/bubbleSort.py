def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr
arr = [73, 5, 91, 28, 64, 12, 100, 47, 3, 86]
bubble_sort(arr)
print(arr)
