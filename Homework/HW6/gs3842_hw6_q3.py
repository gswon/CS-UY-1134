from DoublyLinkedList import *
class CompactString:
    def __init__(self, orig_str):
        self.sdata = DoublyLinkedList()
        for char in orig_str:
            if self.sdata.is_empty():
                self.sdata.add_last((char, 1))
            elif self.sdata.trailer.prev.data[0] == char:
                self.sdata.trailer.prev.data = (char, self.sdata.trailer.prev.data[1] + 1)
            else:
                self.sdata.add_last((char, 1))

    def __add__(self, other):
        add_val = CompactString("")

        for node in self.sdata:
            add_val.sdata.add_last(node)

        if other.sdata.header.next.data[0] == add_val.sdata.trailer.prev.data[0]:
            update_count = add_val.sdata.trailer.prev.data[1] + other.sdata.header.next.data[1]
            add_val.sdata.trailer.prev.data = (add_val.sdata.trailer.prev.data[0], update_count)
            other.sdata.delete_first()

        for node in other.sdata:
            add_val.sdata.add_last(node)

        return add_val

    def __lt__(self, other):
        string1 = self.sdata.header.next
        string2 = other.sdata.header.next

        if string1 == self.sdata.trailer:
            return not other.sdata.is_empty()
        elif string2 == other.sdata.trailer:
            return False

        while string1 != self.sdata.trailer or string2 != other.sdata.trailer:
            if string1.data[0] < string2.data[0]:
                return True
            elif string1.data[0] > string2.data[0]:
                return False
            else:
                if string1.data[1] == string2.data[1]:
                    string1 = string1.next
                    string2 = string2.next
                elif string1.data[1] > string2.data[1]:
                    return False
                elif string1.data[1] < string2.data[1]:
                    return True

        return False


    def __le__(self, other):
        def check(a,b):
            if a.sdata.is_empty() and b.sdata.is_empty():
                return True
            elif len(a.sdata) == 0 and len(b.sdata) == 0:
                return False
            else:
                cm1 = a.sdata.header.next
                cm2 = b.sdata.header.next
                while cm1.data is not None and cm2.data is not None:
                    if cm1.data[0] == cm2.data[0]:
                        if cm1.data[1] == cm2.data[1]:
                            cm1 = cm1.next
                            cm2 = cm2.next
                        else:
                            return cm1.data[1] < cm2.data[1]
                    else:
                        return cm1.data[0] < cm2.data[0]
                if cm1.data is not None and cm2.data is None:
                    return False
                else:
                    return True

        result = check(self, other) or self < other
        return result


    def __gt__(self, other):
        return not(self <= other)

    def __ge__(self, other):
        return not(self < other)

    def __repr__(self):
        return "".join([char * count for char, count in self.sdata])
    
s1 = CompactString('aaz')
s2 = CompactString('aa')
print(s1 > s2)