def remove_all(lst, value=None):
    if value == None:
        raise ValueError

    count = 0
    for i in range(len(lst)):
        if lst[i] == value:
            count += 1
        elif lst[i] != value:
            lst[i-count] = lst[i]

    for j in range(count):
        lst.pop()

    return lst