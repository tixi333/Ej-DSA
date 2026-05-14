l = [ 0, 0, 0, 1, 0, 0]

def propagar(l):
    for i in range(len(l)):
        if l[i] == 1:
            
            j = i + 1
            if i > 0:
                k = i - 1
            
            while k >= 0 and l[k] == 0:
                l[k] = 1
                k -= 1  
                
            while j < len(l) and l[j] == 0:
                l[j] = 1
                j += 1
        
    return l

print(propagar(l))