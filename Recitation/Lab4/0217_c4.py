# Part A: Find the pivot – Time Constraint O(log(n))

def find_pivot(lst):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if ((lst[mid - 1] < lst[mid]) != False) or ((lst[mid] < lst[mid + 1]) != False):
            if (lst[mid-1] < lst[mid]) == False:
                return mid
            elif (lst[mid] < lst[mid+1]) == False:
                return mid + 1
            
        if lst[mid] < lst[left]:
            right = mid
        elif lst[mid] > lst[right]:
            left = mid


# Part B: Find the target value – Time Constraint O(log(n))
def shift_binary_search(lst, target):
    result = find_pivot(lst)
    if lst[result - 1] == target:
        return result - 1
    else:
        return None


def main():
    nums = [15, 20, 21, 1, 3, 6, 7, 10, 12, 14]
    # print(find_pivot(nums))
    print(shift_binary_search(nums, 21))

main()