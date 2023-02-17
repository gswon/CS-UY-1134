### This is the answer from recitation class (나의 풀이랑 살짝 다른 경우 여기에 적어둠.)
### c1 to c4.py file is my own answer and it works well!
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


5)
```Python

```
