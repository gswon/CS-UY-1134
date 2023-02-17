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
      
      
Θ(log(n<sup>5</sup>)) = Θ(5log(n))   
**Answer: Θ(log(n))**
    
     
     
     
     
2)
```python
def func3(n):
    i = 1
    while i < n**1000000:
        i *= 2
        print("*")
```
    
     
**Answer: &Theta;log(n)**
     
     
     
     
     
3)
```python
def func5(n):
    i = 1
    while i < n ** 2:
        i *= 2
        print()
```
   
   
Inside the while loop is constant   
&Theta;(log<sub>2</sub>(n<sup>n</sup>)) = &Theta;(nlog(n))   
**Answer: &Theta;(nlog(n))**
