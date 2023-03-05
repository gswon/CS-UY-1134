## Time Complexcity 

Big O <-- Represents the worst case of time complexcity (= upper bound of the graph)    
&Omega;  <-- Represents the lower bound of the running time (= lower bound of the graph)    
&Omega; ≤ Θ ≤ Big O      

Equation     
--> 1 + 2 + 3 + 4 +...+ n = n(n+1)/2 = Θ(n<sup>2</sup>)    
--> 1 + 2 + 4 + 8 +...+ 2<sup>n+1 </sup> - 1 = Θ(2<sup>n</sup>)       
--> 1 + 2 + 4 + 8 +...+ n = 2n - 1 = Θ(n)  (1 to n is log(n) times)    

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
Answer: Θ(log(n))

<br/>
<br/>


2)
```python
def func3(n):
    i = 1
    while i < n**1000000:
        i *= 2
        print("*")
```
<br/>      
Answer: &Theta;log(n)
<br/>
<br/>
<br/>

3)
```python
def func5(n):
    i = 1
    while i < n ** 2:
        i *= 2
        print()
```  
<br/>

Inside the while loop is constant   
&Theta;(log<sub>2</sub>(n<sup>n</sup>)) = &Theta;(nlog(n))   
**Answer: &Theta;(nlog(n))**
<br/>
<br/>
<br/>
