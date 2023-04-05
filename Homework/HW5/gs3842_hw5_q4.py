from ArrayStack import *

class Queue:
    def __init__(self):
        self.data1 = ArrayStack()
        self.data2 = ArrayStack()
        # self.data2는 dequeue, first method사용할때만 쓰이고
        # 나머지일때는 안쓰이는 방식이 맞는지여부

    def __len__(self):
        return len(self.data1) # len(self) 인지
    
    def is_empty(self):
        return len(self.data1) == 0 # len(Self.data) == 0인지 
    
    def enqueue(self, val):
        self.data1.push(val)

    def dequeue(self):
        if self.data1.is_empty():
            raise Exception("Queue is empty")
        
        for i in range(len(self.data1)-1):
            self.data2.push(self.data1.pop())

        val = self.data1.pop()

        for j in range(len(self.data2)):
            self.data1.push(self.data2.pop())
            
        return val
    # 시간복잡도는 상관없는지
    
    def first(self): # first도 적어야하는지, 더 적어야하는 method있는지 
        if self.data1.is_empty():
            raise Exception("Queue is empty")
        for i in range(len(self.data1)-1):
            self.data2.push(self.data1.pop())

        val = self.data1.pop()
        self.data1.push(val)

        for j in range(len(self.data2)):
            self.data1.push(self.data2.pop())
            
        return val
        