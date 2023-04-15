from DoublyLinkedList import *

def copy_linked_list(lnk_lst):
    dll_copy = DoublyLinkedList()
    for node in lnk_lst:
        dll_copy.add_last(node)

    return dll_copy


def deep_copy_linked_list(lnk_lst):
    dll_copy = DoublyLinkedList()

    for node in lnk_lst:
        if type(node) == DoublyLinkedList:
            dll_copy.add_last(deep_copy_linked_list(node)) 
        else:
            dll_copy.add_last(node)

    return dll_copy


def main():
    lnk_lst1 = DoublyLinkedList()
    elem1 = DoublyLinkedList()
    elem1.add_last(1)
    elem1.add_last(2)
    lnk_lst1.add_last(elem1)
    elem2 = 3
    lnk_lst1.add_last(elem2)

    lnk_lst2 = copy_linked_list(lnk_lst1)
    print(lnk_lst2)

    e1 = lnk_lst2.header.next
    e1_1 = e1.data.header.next
    e1_1.data = 10
    print(lnk_lst2)

    e2 = lnk_lst2.header.next
    e2_1 = e2.data.header.next
    print(e2_1.data)

    lnk_lst1 = DoublyLinkedList()
    elem1 = DoublyLinkedList()
    elem1.add_last(1)
    elem1.add_last(2)
    lnk_lst1.add_last(elem1)
    elem2 = 3
    lnk_lst1.add_last(elem2)

    lnk_lst2 = deep_copy_linked_list(lnk_lst1)
    print(lnk_lst2)

    e1 = lnk_lst1.header.next
    e1_1 = e1.data.header.next
    e1_1.data = 10
    print(lnk_lst2)

    e2 = lnk_lst2.header.next
    e2_1 = e2.data.header.next
    print(e2_1.data)
main()