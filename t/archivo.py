class Nodo:
    def __init__(self, data):
        self.data = data
        self.r_child = None
        self.l_child = None

def in_order(node):
    actual = node
    if actual is None:
        return
    in_order(actual.l_child)
    print(actual.data)
    in_order(actual.r_child)

def pre_order(node):
    actual = node
    if actual is None:
        return
    print(actual.data)
    pre_order(actual.l_child)
    pre_order(actual.r_child)

def post_order(node):
    actual = node
    if actual is None:
        return
    post_order(actual.l_child)
    post_order(actual.r_child)
    print(actual.data)
    
def level_order(node):
    pass