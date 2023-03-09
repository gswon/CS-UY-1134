def list_min(lst, low, high):
    # if low == high:
    #     return lst[low]
    # return min(lst[low], list_min(lst, low+1, high))

    if low == high:
        return lst[low]
    else:
        value = list_min(lst, low+1, high)
        if lst[low] < value:
            return lst[low]
        else:
            return value


def main():
    lst = [1002,3,24,24,0,151,2134,2,1]
    low = 0
    high = len(lst) - 1
    print(list_min(lst, 2, 5))
main()