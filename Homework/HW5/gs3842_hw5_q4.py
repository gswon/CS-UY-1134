from ArrayStack import *

class Queue:
    def __init__(self):
        self.data1 = ArrayStack()
        self.data2 = ArrayStack()

    def __len__(self):
        return (len(self.data1) + len(self.data2))
    
    def is_empty(self):
        return (len(self.data1) + len(self.data2)) == 0
    
    def enqueue(self, val):
        self.data1.push(val)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        elif self.data2.is_empty():
            while self.data1.is_empty() == False:
                self.data2.push(self.data1.pop())
        
        return self.data2.pop()
    
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        elif self.data2.is_empty():
            for i in range(len(self.data1)):
                self.data2.push(self.data1.pop())

        return self.data2.top()

q = Queue()
print(q.is_empty())
print(len(q))
print(q.dequeue())

# q = Queue()
# print(q.is_empty()) # True
# q.enqueue(1)
# q.enqueue(2)
# print(q.first()) # 1
# q.enqueue(3)
# q.enqueue(4)
# print(len(q)) # 4
# print(q.is_empty()) # false
# print(q.dequeue()) # 1
# print(q.dequeue()) # 2
# print(len(q)) # 2
# q.enqueue(100)
# print(q.is_empty()) # false
# print(len(q)) # 3
# print(q.dequeue()) # 3 
# print(q.dequeue()) # 4
# print(q.dequeue()) # 100
# print(len(q)) # 0
# print(q.is_empty()) # True
