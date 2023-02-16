def split_parity(lst):
    position = 0
    right_pointer = len(lst) - 1
    while position < right_pointer:
        if lst[position] % 2 == 0:
            lst[position], lst[right_pointer] = lst[right_pointer], lst[position]
            right_pointer -= 1
        else:
            position += 1