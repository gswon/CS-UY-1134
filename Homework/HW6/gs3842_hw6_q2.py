from DoublyLinkedList import *

class Integer:
    def __init__(self, num_str):
        if num_str == None:
            raise Exception
        
        self.memory = DoublyLinkedList()

        for num in num_str:
            self.memory.add_last(int(num))

    def __add__(self, other):
        combined = Integer("")
        val1 = self.memory.trailer.prev
        val2 = other.memory.trailer.prev
        numbers_put = 0

        while val1 != self.memory.header or val2 != other.memory.header:
            total1 = 0 
            total2 = 0

            if val1 == self.memory.header:
                total1 = 0
            else:
                total1 = val1.data

            if val2 == other.memory.header:
                total2 = 0
            else:
                total2 = val2.data

            total = numbers_put + total1 + total2
            numbers_put = total // 10
            add = total % 10
            combined.memory.add_first(add)
            
            if val1 != self.memory.header:
                val1 = val1.prev

            if val2 != other.memory.header:
                val2 = val2.prev

        if numbers_put != 0:
            combined.memory.add_first(numbers_put)
        
        return combined
    
    def __mul__(self, other):
        a = self.memory.trailer.prev
        b = self.memory.trailer.prev
        

    def __repr__(self):
        final_result = "".join(str(elem) for elem in self.memory).lstrip("0")
        if final_result:
            return final_result
        else:
            return "0"