from ArrayStack import *
from ArrayQueue import *

def permutations(lst):
    stack = ArrayStack()
    queue = ArrayQueue()
    result = []

    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    
    for elem in lst:
        stack.push(elem)
    queue.enqueue([stack.pop()])

    while not stack.is_empty():
        val = stack.pop()
        for i in range(len(queue)):
            lst_val = queue.dequeue()
            for j in range(len(lst_val) + 1):
                queue.enqueue(lst_val[:j]+[val]+lst_val[j:]) # 1
                """
                lst2 = lst_val.copy()
                lst2.insert(j, val)
                queue.enqueue(lst2)
                
                this also works instead of # 1
                """
    
    for i in range(len(queue)):
        result.append(queue.dequeue())

    return result
