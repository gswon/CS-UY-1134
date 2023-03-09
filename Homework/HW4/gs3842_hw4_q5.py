def count_lowercase(s, low, high):
    if low > high:
        return 0
        
    if s[low].islower():
        return 1 + count_lowercase(s, low+1, high)
    else:
        return count_lowercase(s, low+1, high)

def is_number_of_lowercase_even(s, low, high):
    if low == high:
        if s[low].islower():
            return False
        else:
            return True
    else:
        count = is_number_of_lowercase_even(s, low+1, high)
        if s[low].islower():
            return not(count)
        else:
            return count

def main():
    s = "aAvSasdS"
    low = 0
    high = len(s) - 1
    print(count_lowercase(s,low,high))
    print(is_number_of_lowercase_even(s,low,high))
main()