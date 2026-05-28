def peces(A,B):
    abajo = []

    for e in range (len(A)):
        if B[e] == 1:
            abajo.append(A[e])
            A.pop(e)
    


A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]
peces(A,B)