class Nodo:
    def __init__(self, data):
        self.data = data
        self.pointer = None

class singlyLinkedList:
    def __init__(self):
        self.head = None
        
    def create_newnode(self,value):
        new_node = Nodo(value)
        
        if self.head == None:
            self.head = new_node #pointer/
        
        else:
            current = self.head
            while current.pointer != None:
                current = current.pointer
            
            current.pointer = new_node
            
    def search_node(self, value):
                
        if self.head == None:
            return "No values defined yet"
        
        else:
            current = self.head
            while current.pointer != None:
                mem = current.pointer
                current = current.pointer
            
            if current.data == value:
                return f"Required value: {value} is located at: {mem}"
                
                        
    def sort_linkedlist(self):
        if self.head == None:
            print("a")
            return "No enough nodes to sort"
        
        else:
            
            length = 0
            current = self.head

            while current:
                length += 1
                current = current.pointer
            
            for _ in range(length - 1):
                current = self.head

                while current.pointer:
                    if current.data > current.pointer.data:
                        current.data, current.pointer.data = (
                            current.pointer.data,
                            current.data
                        )

                    current = current.pointer
                    
                
                
            return length
                
    def delete_node(self,value):
        
        if self.head == None: # si no hay elementos 
            return "No nodes in linked list"
        
        elif self.head == value: # si el head es el que se desea eliminar
            self.head = self.head.pointer

        else:
            current = self.head

            while current.pointer is not None:
                if current.pointer.data == value: 
                    current.pointer = current.pointer.pointer 
                    return "Deleted"
                current = current.pointer

    def is_empty(self):
        if self.head == None:
            return "True"
        else:
            return "False"

    def print_linkedlist(self):
        lista = []
        current = self.head
        while current != None:
            lista.append(current.data)
            print(current.data)
            current = current.pointer
        
        return lista
        
    def get_size(self):
        contador = 0
        if self.head == None:
            return contador

        else:
            contador = 1
            current = self.head
            while current.pointer != None:
                current = current.pointer
                contador +=1
        
        return contador
    
    def insert_node(self, value, previous):
        new_node = Nodo(value)
        current = self.head

        while current is not None:
            if current.data == previous:
                new_node.pointer = current.pointer
                current.pointer = new_node
                return "inserted"

            current = current.pointer
        
    def invert(self):
        
            
            

singly = singlyLinkedList()
"""
print(f"is empty:", singly.is_empty())
singly.sort_linkedlist()
print(singly.delete_node(3))

print(singly.search_node(3))
"""
singly.create_newnode(2)
singly.create_newnode(8)
singly.create_newnode(5)
singly.create_newnode(4)

print(singly.sort_linkedlist())
print(singly.print_linkedlist())

"""""
print(singly.insert_node(3,2))
print(singly.get_size())

print(singly.print_linkedlist())

print(singly.delete_node(4))
print(singly.search_node(5))
print(singly.is_empty())
"""""
# -----------------------------------------------------------------------------

class Nodo2:
    def __init__(self,data):
        self.data = data
        self.pointer = None
        self.previous = None
        
class doubleLinkedList:
    
    def __init__(self):
        self.head = None
        
    def create_newnode(self, value):
        new_node = Nodo2(value)
        
        if self.head == None:
            self.head = new_node
        
        current = self.head
        
        while current.pointer != None:
            current = current.pointer
            
        current.pointer = new_node
        new_node.previous = current

"""""
double  = doubleLinkedList()    
double.create_newnode(2)
double.create_newnode(4)
double.create_newnode(5)        
"""       
# -----------------------------------------------------------------------------

class Nodo3:
    def __init__(self, data):
        self.data = data
        self.pointer = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def create_newnode(self, value):
        new_node = Nodo3(value)
        
        if self.head ==  None:
            self.head = new_node
            self.head.pointer = self.head
        
        else:
            current = self.head
            
            while current.pointer != self.head:
                current = current.pointer
            
            current.pointer = new_node
            new_node.pointer = self.head
        
# --------------------------------------------------

class Nodo4:
    def __init__(self,data):
        self.data = data
        self.pointer = None
        self.previous = None
        
class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
    
    def create_newnode(self,value):
        new_node = Nodo4(value)
        
        if self.head == None:
            self.head = new_node
            self.head.pointer = self.head
            self.head.previous = self.head
        
        else:
            current = self.head
            
            while current.pointer != self.head:
                current = current.pointer
            
            
            current.pointer = new_node
            new_node.previous = current
            new_node.pointer = self.head
            self.head.previous = new_node