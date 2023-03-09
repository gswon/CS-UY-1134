def appearances(s, low, high):
    if len(s) == 0:
        return {}
    elif low == high:
        return {s[low] : 1}
    else:
        dic = appearances(s, low+1, high)
        if s[low] in dic:
            dic[s[low]] += 1
            return dic
        else:
            dic[s[low]] = 1
            return dic

def main():
    s = "Hello"
    low = 0
    high = len(s) - 1
    print(appearances(s, high, high))
main()