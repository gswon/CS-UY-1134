from stacks_code_lab import *

def flatten_list(lst):
    stack = ArrayStack()
    
    while len(lst) != 0:
        val = lst.pop() # get the last value
        if isinstance(val, list): # is it a list?
            lst.extend(val) # extend it back
        else:
            stack.push(val)
    
    while not stack.is_empty():
        lst.append(stack.pop()) # remove the values the stack and place back into the list


lst = [1,[2,3,4],[5,[6,7],[[[8]],[[9]]]]]
print(lst)
flatten_list(lst)
print(lst)