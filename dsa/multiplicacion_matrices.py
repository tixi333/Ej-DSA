import matplotlib.pyplot as plt
import math

A = [
    [1, 2, 3],
    [4, 5, 6]
] # 1

B = [
    [7, 8],
    [9, 10],
    [11, 12]
] #1

result = [
    [0, 0],
    [0, 0]
] #1

for i in range(len(A)): # n

    for j in range(len(B[0])): # n

        for k in range(len(B)): # n

            result[i][j] += A[i][k] * B[k][j] # 2

print(result)
# 3 + 2n3

x = []
y = []

for n in range(1, 50):

    op = 3 + 2*(n**3)

    x.append(n)
    y.append(op)

plt.plot(x, y)

plt.title("Operaciones en búsqueda lineal")
plt.xlabel("Tamaño del array (n)")
plt.ylabel("Cantidad de operaciones")

plt.show()