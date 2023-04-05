from ArrayStack import *

class MaxStack:
    def __init__(self):
        self.data = ArrayStack()
        self.maximum = None

    def is_empty(self):
        return self.data.is_empty()
    
    def __len__(self):
        return len(self.data)
    
    def push(self, e):
        if self.is_empty():
            self.maximum = e
        else:
            if self.data.top()[0] < e:
                self.maximum = e

        tup = (e, self.maximum)
        self.data.push(tup)

    def top(self):
        if self.is_empty():
            raise Exception("MaxStack is empty")
        return self.data.top()[0]
    
    def pop(self):
        if self.is_empty():
            raise Exception("MaxStack is empty")
        else:
            val = self.data.pop()
            if self.is_empty():
                self.maximum = None
            self.maximum = self.data.top()[1]

        return val[0]
    
    def max(self):
        if self.is_empty():
            raise Exception("MaxStack is empty")
        return self.maximum