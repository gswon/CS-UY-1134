def two_sum(srt_lst, target):
    position = 0
    right_pointer = len(srt_lst) - 1
    while position < right_pointer:
        if srt_lst[position] + srt_lst[right_pointer] == target:
            return (position, right_pointer)
        elif srt_lst[position] + srt_lst[right_pointer] < target:
            position += 1
        else:
            right_pointer -= 1