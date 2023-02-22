### This is the answer from recitation class (나의 풀이랑 살짝 다른 경우 여기에 적어둠.)
#### c1 to c4.py files are my own answer!

<br></br>
3-b)
```Python
def find_missing2(lst):
    left = 0
    right = len(lst) - 1
    if lst[0] != 0:
        return 0
    elif lst[-1] == len(lst) - 1:
        return len(lst)
    
    while left <= right:
        mid = (left + right) // 2

        if mid == lst[mid]:
            left = mid + 1
        elif mid == lst[mid - 1]:
            right = mid - 1
        else:
            return mid
```

Optional 5-a)
```Python
def jump_search(lst, val, k):
    if len(lst) == 0:
        return None

    curr = 0
    prev = curr
    jump = k

    while curr < len(lst) and lst[curr] < val:
        prev = curr
        curr += jump

    if curr >= len(lst):
        prev = curr - jump
        curr = len(lst) - 1

    while curr >= prev:
        if lst[curr] == val:
            return curr
        curr -= 1

    return None

# Test Code
print(jump_search([1, 3, 6, 7, 10, 12, 15, 20, 22, 24, 29, 33, 39, 55, 61, 64, 99, 101, 134, 150], 15, 4))
```
