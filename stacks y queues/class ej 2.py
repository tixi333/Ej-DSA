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

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)
    
    def peek(self):
        first = self.items[0]
        return first
    
    def is_empty(self):
        return True if self.items == [] else False
    
    def size(self):
        size = len(self.items)
        return size
    
pila = Stack()

pila.push(14)
pila.push(20)
pila.push(13)

print("\tStack:")
print(f" - removed: {pila.pop()}")
print(f" - last: {pila.peek()}")
print(f" - size: {pila.size()}")
print(f" - empty: {pila.is_empty()}")

fila = Queue()
fila.enqueue(14)
fila.enqueue(20)
fila.enqueue(13)

print("\tQueue:")
print(f" - removed: {fila.dequeue()}")
print(f" - first: {fila.peek()}")
print(f" - size: {fila.size()}")
print(f" - empty: {fila.is_empty()}")
