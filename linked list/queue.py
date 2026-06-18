from linkedlist import singlyLinkedList

class Queue:
    def __init__(self):
        self.items = singlyLinkedList()

    def enqueue(self, item):
        self.items.create_newnode(item)

    def dequeue(self):
        if self.items.head is None:
            return "Queue is empty"

        value = self.items.head.data
        self.items.head = self.items.head.pointer

        return value

    def peek(self):
        if self.items.head is None:
            return "Queue is empty"

        return self.items.head.data

    def is_empty(self):
        return self.items.head is None

    def size(self):
        contador = 0
        current = self.items.head

        while current is not None:
            contador += 1
            current = current.pointer

        return contador