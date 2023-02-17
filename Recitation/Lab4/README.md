### This is the answer from recitation class (나의 풀이랑 살짝 다른 경우만 적어둠.)

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
