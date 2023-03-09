def split_by_sign(lst, low, high):
    if low >= high:
        return lst
    else:
        if lst[low] >= 0 and lst[high] < 0:
            lst[low], lst[high] = lst[high], lst[low]
            return split_by_sign(lst, low+1, high - 1)
        elif lst[low] >= 0 and lst[high] >= 0:
            return split_by_sign(lst, low, high-1)
        elif lst[low] < 0 and lst[high] >= 0:
            return split_by_sign(lst, low, high-1)
        else:
            return split_by_sign(lst, low+1, high)


def main():
    # left neg, right pos (pos-1)
    # left neg, right neg (neg+1)
    # left pos, right pos (right pos-1)
    # left pos, right neg (change)
    lst = [-100,1,-2,1,-1,1,23,-2,5,2,-9,100,-4]
    high = len(lst) - 1
    print(split_by_sign(lst,0,high))
    print(lst)
main()