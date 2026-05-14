import matplotlib.pyplot as plt
import math

arr = [3, 5, 6, 8, 9, 12, 14, 17, 23, 31] #1

searchedvar = 6 #1

left = 0 #1
right = len(arr) - 1 # 2

while left <= right: # log n -- va disminuyendo

    mid = (left + right) // 2 #3

    if arr[mid] == searchedvar:  #1
        print(f"{searchedvar} at index {mid}")
        break

    elif arr[mid] < searchedvar:  #1
        left = mid + 1 #1

    else: 
        right = mid - 1 #1

# 5 + 7 log n

x = []
y = []

for n in range(1, 101):

    op = 5 + 7 * math.log2(n)

    x.append(n)
    y.append(op)

plt.plot(x, y)

plt.title("Operaciones en búsqueda binaria")
plt.xlabel("Tamaño del array (n)")
plt.ylabel("Cantidad de operaciones")

plt.show()