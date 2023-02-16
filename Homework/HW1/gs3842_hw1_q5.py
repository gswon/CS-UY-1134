def fibs(n):
    previous_num = 0
    num = 1
    for i in range(n):
        yield num
        previous_num, num = num, previous_num + num