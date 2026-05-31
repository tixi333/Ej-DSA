def peces(A,B):
    abajo = []
    e = 0
    while e < len(A):
        if B[e] == 1:
            abajo.append(A[e])
            A.pop(e)
            B.pop(e)
        
        else:

            if len(abajo)> 0:
                for i in range(len(abajo)):
                    if A[e] > abajo[-1-i]:
                        abajo.pop(-1-i)
                    else:
                        A.pop(e)
                        B.pop(e)
                        
            else:
                e += 1
        
    return A
    
A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]
peces(A,B)