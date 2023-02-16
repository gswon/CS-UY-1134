def sum_num1(n):
    result = 0
    for i in range(1, n):
        result += i*i
    return result

def sum_num2(n):
    return sum([i*i for i in range(1, n)])

def sum_num3(n):
    result = 0
    for i in range(1, n):
        if i % 2 != 0:
            result += i*i
    return result

def sum_num4(n):
    return sum([i*i for i in range(1, n) if i % 2 != 0])