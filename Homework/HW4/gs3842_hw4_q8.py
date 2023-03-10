def flat_list(nested_lst, low, high):
    if len(nested_lst) == 0:
        return []
    elif low > high:
        return []
    else:
        lst = flat_list(nested_lst, low+1, high)
        if isinstance(nested_lst[low], int):
            return [nested_lst[low]] + lst
        else:
            lst_in = nested_lst[low]
            high = len(lst_in) - 1
            return flat_list(lst_in, 0, high) + lst


def main():
    nested_lst = [[[1]],[2,3,4,[5],6,9,[10]]]
    low = 0
    high = len(nested_lst) - 1
    print(flat_list(nested_lst, low, high))
main()