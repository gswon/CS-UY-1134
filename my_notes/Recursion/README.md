이렇게 생각하면서 문제풀기    
    
```Python
def is_number_of_lowercase_even(s, low, high):   
    if low == high:    # 여기는 s가 하나일때, 가장 마지막일때를 생각하고 만듬 // base case
        if s[low].islower():
            return False
        else:
            return True
    else:
        count = is_number_of_lowercase_even(s, low+1, high)  # 이건 무조건 low+1부터 high까지 돈다는것을 가정한다
        if s[low].islower():  # 여기는 is_number_of_lowercase_even 함수가 low일때를 생각해서 만듬. 왜냐하면 위에 count는 low+1부터 high까지만 돌기 때문이다
            return not(count)
        else:
            return count
```
