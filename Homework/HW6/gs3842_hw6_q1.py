from DoublyLinkedList import *

class LinkedQueue:
    def __init__(self):
        self.lque = DoublyLinkedList()
    
    def __len__(self):
        return len(self.lque)
    
    def is_empty(self):
        return len(self.lque) == 0
    
    def enqueue(self, val):
        self.lque.add_last(val)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            return self.lque.delete_first()
        
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            return self.lque.header.next.data