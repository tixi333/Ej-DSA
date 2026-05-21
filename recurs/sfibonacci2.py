def fibonacci(n):
    if n == 0 :
        return 0
    
    elif n == 1:
        return 1
    
    else:
        return fibonacci(n-1) + fibonacci(n-2)



pos = int(input("Posición de la serie de Fibonacci: "))
numf = fibonacci(pos)
print(f"El número en la posición {pos} de la serie de Fibonacci es: {numf}")