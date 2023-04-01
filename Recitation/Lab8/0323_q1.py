from stacks_code_lab import *

def stack_sum(s):
    if len(s) == 0:
        return 0
    else:
        val = s.pop()
        curr_total = stack_sum(s)
        curr_total += val
        s.push(val)
        return curr_total

def stack_num2(s):
    total = 0
    if not s.is_empty():
        val = s.pop()
        total = val + stack_num2(s)
        s.push(val)
    return total


s = ArrayStack()
lst = [1,-14,5,6,-7,9,10,-5,-8]
for i in lst:
    s.push(i)
print(stack_sum(s))
print(stack_num2(s))
