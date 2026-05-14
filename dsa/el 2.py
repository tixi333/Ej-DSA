import matplotlib.pyplot as plt
arr = [4, 7, 2, 9, 7, 5, 2, 11, 8, 4] #1

n = len(arr) #2
is_repeated = False # !

for i in range(n): # n veces
    for e in range(i+ 1, n): #n veces
        if arr[i] == arr[e]: # 1
            is_repeated = True #1
            
        
if is_repeated == True:
    print("hay repetidos")
else:
    print("todos son unicos :)")
    
# 4 + 2n2 operaciones
x = []
y = []

for n in range(1, 21):

    op = 4 + 2*(n**2)

    x.append(n)
    y.append(op)

plt.plot(x, y)

plt.title("Elementos únicos - Brute Force")
plt.xlabel("Tamaño del array (n)")
plt.ylabel("Cantidad de operaciones")

plt.show()