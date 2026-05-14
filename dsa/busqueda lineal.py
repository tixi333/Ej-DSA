import matplotlib.pyplot as plt

arr = [12, 5, 8, 23, 17, 3, 14, 9, 31, 6] #1

searchedval = 31 #1
n = len(arr) #1 o 2

for i in range(n): # n 
    if searchedval == arr[i]: # n
        print(f"{searchedval} founded at index {i}") # 1 -- omitir
        break

x = []
y = []

for n in range(1, 11):

    op = 3 + 2*n

    x.append(n)
    y.append(op)

plt.plot(x, y)

plt.title("Operaciones en búsqueda lineal")
plt.xlabel("Tamaño del array (n)")
plt.ylabel("Cantidad de operaciones")

plt.show()