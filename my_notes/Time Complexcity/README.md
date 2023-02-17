## Time Complexcity 

### Example Questions

1)
```python
def func2(n):
    i = 1
    while i < n**5:
        i *= 2
        print("*")
```

Θ(log(n^5)) = Θ(5log(n))
Answer: Θ(log(n))





2)
```python
def func3(n):
    i = 1
    while i < n**1000000:
        i *= 2
        print("*")
```


Answer: &Theta;log(n)
