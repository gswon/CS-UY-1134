from DoublyLinkedList import *

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_sublists(lst1, lst2, result):
        if lst1 == srt_lnk_lst1.trailer and lst2 == srt_lnk_lst2.trailer:
            return result
        else:
            if lst1 == srt_lnk_lst1.trailer:
                result.add_last(lst2.data)
                return merge_sublists(lst1, lst2.next, result)
            elif lst2 == srt_lnk_lst2.trailer:
                result.add_last(lst1.data)
                return merge_sublists(lst1.next, lst2, result)
            elif lst1.data < lst2.data:
                result.add_last(lst1.data)
                return merge_sublists(lst1.next, lst2, result)
            elif lst1.data >= lst2.data:
                result.add_last(lst2.data)
                return merge_sublists(lst1, lst2.next, result)
    
    result = DoublyLinkedList()
    put_lst1 = srt_lnk_lst1.header.next
    put_lst2 = srt_lnk_lst2.header.next
    return merge_sublists(put_lst1, put_lst2, result)

def main():
    lst1 = DoublyLinkedList()
    lst1.add_last(1)
    lst1.add_last(3)
    lst1.add_last(5)
    lst1.add_last(6)
    lst1.add_last(8)

    lst2 = DoublyLinkedList()
    lst2.add_last(9)
    lst2.add_last(10)
    lst2.add_last(100)
    lst2.add_last(10)
    lst2.add_last(15)
    lst2.add_last(15)

    merged_list = merge_linked_lists(lst1, lst2)
    print(merged_list)


if __name__ == "__main__":
    main()