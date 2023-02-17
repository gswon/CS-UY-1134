# 2 - b

def find_missing(lst):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if (lst[mid - 1] + 1 != lst[mid]) or (lst[mid] + 1 != lst[mid + 1]):
            if (lst[mid] + 1 != lst[mid + 1]):
                return (lst[mid + 1] + lst[mid]) // 2
            else:
                return (lst[mid] + lst[mid - 1]) // 2

        if (right - mid) != (lst[right] - lst[mid]):
            left = mid
        elif (left - mid) != (lst[left] - lst[mid]):
            right = mid

        



def main():
    lst = [-1,1,2,3,4,5]
    print(find_missing(lst))
main()