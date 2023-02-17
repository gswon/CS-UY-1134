def reverse_vowels(input_str):
    list_str = list(input_str)
    left = 0
    right = len(list_str) - 1
    vowels_lst = ['a', 'e', 'i', 'o', 'u']
    while left <= right:
        # if (list_str[left] == "a" or list_str[left] == 'e' or list_str[left] == 'i' or list_str[left] == 'o' or list_str[left] == 'u') and (list_str[right] == "a" or list_str[right] == 'e' or list_str[right] == 'i' or list_str[right] == 'o' or list_str[right] == 'u'):
        if (list_str[left] in vowels_lst and list_str[right] in vowels_lst):
            list_str[left], list_str[right] = list_str[right], list_str[left]
            left += 1
            right -= 1
        elif (list_str[left] == "a" or list_str[left] == 'e' or list_str[left] == 'i' or list_str[left] == 'o' or list_str[left] == 'u') != True:
            left += 1
        else:
            right -= 1

    return "".join(list_str)

def main():
    test_string = "tandonn"
    check = reverse_vowels(test_string)
    print(check)
main()