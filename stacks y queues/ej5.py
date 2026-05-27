def invertir_lista(lista):
    stack = []
    for i in range(0,len(lista)):
        e = lista.pop()
        stack.append(e)
    
    for i in range(0, len(stack)):
        e = stack.pop(0)
        lista.append(e)

    return lista

lista= [12, 5, 8, 23, 17, 3, 14, 9, 31, 6]
listaI = invertir_lista(lista)
print(listaI)