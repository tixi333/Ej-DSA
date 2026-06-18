from linkedlist import singlyLinkedList

class Stack:
    def __init__(self):
        self.items = singlyLinkedList()

    def push(self, item):
        self.items.create_newnode(item)

    def pop(self):
        if self.items.head is None:
            return "Stack is empty"

        if self.items.head.pointer is None:
            value = self.items.head.data
            self.items.head = None
            return value

        current = self.items.head

        while current.pointer.pointer is not None:
            current = current.pointer

        value = current.pointer.data
        current.pointer = None

        return value

    def peek(self):
        if self.items.head is None:
            return "Stack is empty"

        current = self.items.head

        while current.pointer is not None:
            current = current.pointer

        return current.data

    def is_empty(self):
        return self.items.head is None

    def size(self):
        contador = 0
        current = self.items.head

        while current is not None:
            contador += 1
            current = current.pointer

        return contador