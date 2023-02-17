def is_palindrome(s):
    left_pointer = 0
    right_pointer = len(s) - 1
    while left_pointer <= right_pointer:
        if s[left_pointer] != s[right_pointer]:
            return False
        else:
            left_pointer += 1
            right_pointer -= 1
    return True

def main():
    test_string = "1race2ar1"
    print(is_palindrome(test_string))
main()
