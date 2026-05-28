def verificación_string(string):
    
    stack = []

    par = {
        "}":"{",
        "]" : "[",
        ")" : "("
    }

    for char in string:
        if char in par:
            if stack == []:
                return 0
            
            else:
                if par[char] == stack[-1]:
                    stack.pop()
        else:
            stack.append(char)
    
    return 1 if stack == [] else 0
    
print(verificación_string(""))
print(verificación_string("}{[(}]}"))
print(verificación_string("{[()()]}"))
print(verificación_string("{[(}]}"))