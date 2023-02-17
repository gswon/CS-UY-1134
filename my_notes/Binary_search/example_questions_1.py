"""
Given a list of sorted elements with some elements occuring more than once, find the first and last
occurence of the target in O(log(n)) runtime. The output must be in a tuple in the given format:
(fist, last)
"""



# answer below : using two binary search
def target_first_last(lst, target):
    first, last = None, None
    if lst[0] == target:
        first = 0
    if lst[-1] == target:
        last= len(lst) - 1
    low, high = 0, len(lst) - 1
    if first is None:
        # binary search for first occurence for the entire list
        while low <= high:
            mid = (low + high) // 2
            if lst[mid] == target and lst[mid - 1] != target:
                first = mid
                low, high = first, len(lst) - 1
                break
            elif lst[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
    if last is None:
        # binary search from first occurence to the rest of the list
        while low <= high:
            mid = (low + high) // 2
            if lst[mid] == target and lst[mid + 1] != target:
                last = mid
                break
            elif lst[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
    result = (first, last)
    return result

lst = [1,3,3,4,5,8,8,12]
print(target_first_last(lst, 8))
