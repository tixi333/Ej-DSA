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
            print(new_node.data)
        
        else:
            current = self.head
            while current.pointer != None:
                current = current.pointer
            
            current.pointer = new_node
            print(new_node.data)
            
        def search_node(self):
            pass
        
        def sort_linkedlist(self):
            pass
            
singly = singlyLinkedList()

singly.create_newnode(2)
singly.create_newnode(4)
singly.create_newnode(5)

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

double  = doubleLinkedList()    
double.create_newnode(2)
double.create_newnode(4)
double.create_newnode(5)        
        
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