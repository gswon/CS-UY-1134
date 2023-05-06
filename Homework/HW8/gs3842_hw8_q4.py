from BinarySearchTreeMap import *

def find_min_abs_difference(bst):
    def helper(node, val, key1):
        if node is None:
            return (val, key1)
        else:
            get = helper(node.left, val, key1)
            val1 = get[0]
            val2 = get[1]
            
            if val2 is not None:
                val = abs(node.item.key - val2)
                if val1 is None:
                    val1 = val
                elif val < val1:
                    val1 = val

            val2 = node.item.key
            return helper(node.right, val1, val2)
        
    if bst.is_empty():
        raise Exception("Can't evaluate min")
    elif len(bst) == 1:
        raise Exception("Can't evaluate min")
    else:
        get = helper(bst.root, None, None)
        return get[0]