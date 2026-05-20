def fibonacci(n):
    n1 = 0
    n2 = 1
    pos = 0
    
    while pos < n:
        numf = n1 + n2
        n1 = n2
        n2 = numf
        pos += 1
    else:
        return n1

pos = int(input("Posición de la serie de Fibonacci: "))
numf = fibonacci(pos)
print(f"El número en la posición {pos} de la serie de Fibonacci es: {numf}")