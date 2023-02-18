def find_missing(lst):
    lst_2 = [i for i in range(len(lst) + 1)]
    '''for i in lst_2:
        if i not in lst:
            return i'''
    sum1 = sum(lst_2)  # linear time complexcity
    sum2 = sum(lst)    # linear time complexcity
    return sum1 - sum2


def main():
    lst = [8,6,0,4,3,5,1,2]
    print(find_missing(lst))
main()
