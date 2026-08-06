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

class Nodo:
    def __init__(self, data):
        self.data = data
        self.r_child = None
        self.l_child = None

def post_order(node):
    actual = node
    if actual is None:
        return
    post_order(actual.l_child)
    post_order(actual.r_child)
    print(actual.data)

def eso (exp):
    stack = Stack()
    conj = exp.split()
    for e in conj:
        
        nodo = Nodo(e)
        if e in ["+","-","*"]:
            print(nodo.data)
            nodo.r_child = stack.pop()
            nodo.l_child = stack.pop()
            stack.push(nodo)
        else:
            stack.push(nodo)
        print(stack.peek())

    am = stack.peek()
    post_order(am)

eso("4 5 + 5 3 - *")