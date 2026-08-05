class Nodo:
    def __init__(self, data):
        self.data = data
        self.r_child = None
        self.l_child = None

n1 = Nodo("raiz")
n2 = Nodo("hijo izq")
n3 = Nodo("hijo derecho")
n4 = Nodo("nieto izq")
n5 = Nodo ("nieto derecho")

def in_order(node):
    actual = node
    if actual is None:
        return
    in_order(actual.left_child)
    print(actual.data)
    in_order(actual.right_child)

def pre_order(node):
    actual = node
    if actual is None:
        return
    print(actual.data)
    pre_order(actual.left_child)
    pre_order(actual.right_child)

def post_order(node):
    actual = node
    if actual is None:
        return
    post_order(actual.left_child)
    post_order(actual.right_child)
    print(actual.data)
    
def level_order(node):
    pass