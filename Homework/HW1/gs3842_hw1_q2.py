def shift(lst, k, direction = 'left'):
    if direction == 'left':
        for i in range(k):
            val = lst[0]
            lst.remove(val)
            lst.append(val)
    else:
        for i in range(k):
            val = lst.pop()
            lst.insert(0, val)