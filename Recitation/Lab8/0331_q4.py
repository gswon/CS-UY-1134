"""
Implement a Stack using just a Queue as the main underlying data collection.
You may only access the ArrayQueue’s methods 
which include: len, is_empty, enqueue, dequeue, and first.
"""
from QueueCode import *

class QueueStack:
    def __init__(self):
        self.data = ArrayQueue()

    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return self.data.is_empty()
    
    def push(self, e):
        self.data.enqueue(e)
    
    def pop(self):
        if self.is_empty():
            raise Exception("QueueStack is empty")
        for i in range(len(self.data) - 1):
            x = self.data.dequeue()
            self.data.enqueue(x)
        
        return self.data.dequeue()
    
    def top(self):
        if self.is_empty():
            raise Exception("QueueStack is empty")
        for i in range(len(self.data) - 1):
            x = self.data.dequeue()
            self.data.enqueue(x)
        
        val = self.data.first()
        self.data.enqueue(self.data.dequeue())

        return val
    
    