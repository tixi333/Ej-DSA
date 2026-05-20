def factorial(n):
    if n == 0:
        return 1
    else:
        print(n)
        return n * factorial(n - 1)


n = int(input("Ingrese un número para calcular su factorial: "))
print(factorial(n))
