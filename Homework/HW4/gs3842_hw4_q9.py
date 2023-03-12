def permutations(lst, low, high):
    if len(lst) == 0:
        return []
    elif low == high:
        return [[lst[low]]]
    else:
        result = []
        lst2 = permutations(lst, low+1, high)
        for num in lst2:
            for i in range(len(num)+1):
                add = list(num)
                add.insert(i, lst[low])
                result.append(add)
         
        result_2 = []
        for lst_in in result:
            if lst_in not in result_2:
                result_2.append(lst_in)

        return result_2
    

def main():
    lst=[1, 3, 3]
    high = len(lst) - 1
    print(permutations(lst,0,2))
    print()
    lst1 = [1,2,3,4]
    high = len(lst1)-1
    print(permutations(lst1,0,high))
    print()
    print(permutations(lst1,2,high))
main()