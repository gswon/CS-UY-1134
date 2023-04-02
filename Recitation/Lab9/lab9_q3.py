from ArrayQueue import *

def flatten_list_by_depth(lst):
    q = ArrayQueue()
    new_lst = []

    for elem in lst:
        q.enqueue(elem)
    
    while not q.is_empty():
        length = len(q)
        for i in range(length):
            front = q.dequeue()
            if isinstance(front, list):
                for elem in front:
                    q.enqueue(elem)
            elif isinstance(front, int):
                new_lst.append(front)

    return new_lst

lst = [[[[0]]], [1,2], 3, [4,[5,6,[7]],8],9]
new_lst = flatten_list_by_depth(lst)
print(new_lst) 