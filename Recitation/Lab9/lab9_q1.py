from ArrayQueue import *

class MeanQueue:
    def __init__(self):
        self.data = ArrayQueue()
        self.qsum = 0

    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return self.data.is_empty()
    
    def enqueue(self, e):
        if not isinstance(e, int) or isinstance(e, float):
            raise TypeError
        else:
            self.data.enqueue(e)
            self.qsum += e
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Meanqueue is empty")
        val = self.data.dequeue()
        self.qsum -= val
        return val
    
    def first(self):
        if self.is_empty():
            raise Exception("Meanqueue is empty")
        return self.data.first()
    
    def sum(self):
        return self.qsum
    
    def mean(self):
        return self.qsum / len(self.data)
    

class ArrayDeque:
    INITIAL_CAPACITY = 8

    def __init__(self):
        self.data_arr = make_array(ArrayDeque.INITIAL_CAPACITY)
        self.num_of_elems = 0
        self.front_ind = None
        self.back_ind = None

    def __len__(self):
        return self.num_of_elems
    
    def is_empty(self):
        # if self.num_of_elems == 0:
        #     return True
        # else:
        #     return False
        return (self.num_of_elems == 0)
    
    def first(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.data_arr[self.front_ind]

    def last(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.data_arr[self.back_ind]
    
    def resize(self, new_cap):
        old_data = self.data_arr
        new_data = make_array(new_cap)
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            new_data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.data = new_data
        self.front_ind = 0
        self.back_ind = self.front_ind + self.num_of_elems - 1
    
    def last(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        
    def enqueue_first(self, elem):
        if self.num_of_elems == len(self.data_arr):
            self.resize(2 * len(self.data_arr))
        if self.is_empty():
            self.data_arr[0] = elem
            self.front_ind = 0
            self.num_of_elems = 1
            self.back_ind = 0
        else:
            self.front_ind = (self.front_ind - 1) % len(self.data_arr)
            self.data_arr[self.front_ind] = elem
            self.num_of_elems += 1
    
    def enqueue_last(self, elem):
        if self.num_of_elems == len(self.data_arr):
            self.resize(2 * len(self.data_arr))
        if self.is_empty():
            self.back_ind = 0
            self.front_ind = 0
            self.num_of_elems = 1
            self.data_arr[0] = elem
        else:
            self.back_ind = (self.back_ind + 1) % len(self.data_arr)
            self.data_arr[self.back_ind] = elem
            self.num_of_elems += 1
    
    def dequeue_first(self):
        if self.is_empty():
            raise Exception("ArrayDeque is empty")
        val =  self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.num_of_elems -= 1
        self.front_ind = (self.front_ind + 1) % len(self.data_arr)
        
        if self.is_empty():
            self.front_ind = None
            self.back_ind = None
        elif self.num_of_elems < len(self.data_arr) // 4:
            self.resize(len(self.data_arr) // 2)

        return val

    def dequeue_last(self):
        if self.is_empty():
            raise Exception("ArrayDeque is empty")
        val = self.data_arr[self.back_ind]
        self.data_arr[self.back_ind] = None
        self.num_of_elems -= 1
        self.back_ind = (self.back_ind - 1) % len(self.data_arr)
        
        if self.is_empty():
            self.front_ind = None
            self.back_ind = None
        elif self.num_of_elems < len(self.data_arr) // 4:
            self.resize(len(self.data_arr) // 2)
            
        return val

