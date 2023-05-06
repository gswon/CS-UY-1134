from BinarySearchTreeMap import *

def create_chain_bst(n):
    bst = BinarySearchTreeMap()
    for i in range(1, n+1):
        bst[i] = None
    return bst

def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst

def add_items(bst, low, high):
    if low > high:
        return bst
    mid = (low + high) // 2
    bst[mid] = None
    add_items(bst, low, mid-1)
    add_items(bst, mid+1, high)