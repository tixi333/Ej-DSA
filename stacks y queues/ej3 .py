def transfer(s,t):
    
    for i in range(0,len(s)):
        e = s.pop()
        t.append(e)
    
    return t


s = [12, 5, 8, 23, 17, 3, 14, 9, 31, 6]
t2 = transfer(s, t = [])
print(t2)