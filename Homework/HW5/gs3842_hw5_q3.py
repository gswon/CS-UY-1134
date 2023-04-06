from ArrayStack import *
from ArrayDeque import *

class MidStack:
    def __init__(self):
        self.stk = ArrayStack()
        self.dque = ArrayDeque()

    def is_empty(self):
        return (self.stk.is_empty() and self.dque.is_empty())
    
    def __len__(self):
        return (len(self.stk) + len(self.dque))
    
    def push(self, e):
        if len(self.stk) == 0:
            self.stk.push(e)
        elif (len(self.stk) + len(self.dque)) % 2 == 0:
            self.stk.push(self.dque.dequeue_first())
            self.dque.enqueue_last(e)
        else:
            self.dque.enqueue_last(e)
    
    def top(self):
        if len(self) == 0:
            raise Exception("MidStack is empty")
        elif len(self) == 1:
            return self.stk.top()
        else:
            return self.dque.last()
    
    def pop(self):
        if len(self) == 0:  # 여기서의 self는 self.stk + self.dque를 다 포함하는건지 여부
            raise Exception("MidStack is empty")
        elif len(self) == 1:
            return self.stk.pop()
        elif len(self) % 2 == 0:
            return self.dque.dequeue_last()
        else:
            val = self.dque.dequeue_last()
            self.dque.enqueue_first(self.stk.pop())
            return val

    def mid_push(self, e):
        if len(self) == 0:
            self.stk.push(e)
        elif len(self.stk) == len(self.dque):
            self.stk.push(e)
        elif len(self.stk) > len(self.dque):
            self.dque.enqueue_first(e)


midS = MidStack()

midS.mid_push(3)
midS.push(2)
midS.mid_push(10)
print(midS.pop())
print(midS.pop())
print(midS.pop())

midS.push(7)
midS.push(7)
midS.push(7)
midS.test()

# print(f"top = {midS.top()}")

# midS.push(4)
# midS.push(6)
# midS.push(8)
# midS.push(10)
# midS.mid_push(12)

# print(f"top = {midS.top()}")

# print(midS.pop())
# print(midS.pop())
# print(midS.pop())
# print(midS.pop())
# print(midS.pop())
# print(midS.pop())