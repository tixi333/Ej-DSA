from archivo import in_order, post_order, pre_order, Nodo

class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        last = self.items[-1]
        return last
    
    def is_empty(self):
        return True if self.items == [] else False
    
    def size(self):
        size = len(self.items)
        return size

def parser (exp):
    stack = Stack()
    conj = exp.split()
    for e in conj:
        
        nodo = Nodo(e)
        if e in "+-*":
            nodo.r_child = stack.pop()
            nodo.l_child = stack.pop()
            stack.push(nodo)
        else:
            stack.push(nodo)

    am = stack.peek()
    post_order(am)

parser("4 5 + 5 3 - *")