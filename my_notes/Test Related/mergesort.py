def merge_sort(lst):
    if len(lst) == 0:
        return lst
    elif len(lst) == 1:
        return lst
    else:
        mid = (0 + len(lst) - 1) // 2
        left_lst = lst[:mid+1]
        right_lst = lst[mid+1:]
        merge_sort(left_lst)
        merge_sort(right_lst)
        merged = merge(left_lst, right_lst)
        lst[:] = merged[:]

def merge(srt_lst1, srt_lst2):
    merged_lst = []
    i1 = 0
    i2 = 0
    while ((i1 < len(srt_lst1)) and (i2 < len(srt_lst2))):
        if srt_lst1[i1] < srt_lst2[i2]:
            merged_lst.append(srt_lst1[i1])
            i1 += 1
        else:
            merged_lst.append(srt_lst2[i2])
            i2 += 1

    while i1 < len(srt_lst1):
        merged_lst.append(srt_lst1[i1])
        i1 += 1
    
    while i2 < len(srt_lst2):
        merged_lst.append(srt_lst2[i2])
        i2 += 1
    return merged_lst

lst = [1,9,7,5,0,10,2,6]
merge_sort(lst)
print(lst)