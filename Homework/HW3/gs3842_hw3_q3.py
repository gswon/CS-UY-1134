def find_duplicates(lst):
    result = []
    biggest_num = max(lst)
    lst2 = (biggest_num + 1) * [0]

    for i in range(len(lst)):
        lst2[lst[i]] += 1

    for j in range(len(lst2)):
        if lst2[j] > 1:
            result.append(j)

    return result