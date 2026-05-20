def cuenta_regresiva(n):
    if n == 0:
        return "boom!"
    else:
        print(n)
        cuenta_regresiva(n - 1)
    
n = int(input("Ingrese un número para la cuenta regresiva: "))
cuenta_regresiva(n)