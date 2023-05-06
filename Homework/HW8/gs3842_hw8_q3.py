from BinarySearchTreeMap import *

def restore_bst(prefix_lst):
    def helper(left, right, pos):
        if left > right:
            return (None, pos)
        else:
            key = prefix_lst[pos]
            get = BinarySearchTreeMap.Item(key)
            root = BinarySearchTreeMap.Node(get)
            pos += 1

            if left == right:
                return (root, pos)
            else:
                pos1 = pos
                while pos1 <= right and prefix_lst[pos1] < root.item.key:
                    pos1 += 1
                
                tup = helper(pos, pos1 - 1, pos)
                root.left = tup[0]
                pos = tup[1]

                if root.left:
                    root.left.parent = root
                
                tup_2 = helper(pos1, right, pos)

                root.right = tup_2[0]
                pos = tup_2[1]

                if root.right:
                    root.right.parent = root

                return (root, pos)

    if len(prefix_lst) == 0:
        return BinarySearchTreeMap()
    elif len(prefix_lst) == 1:
        val = prefix_lst[0]
        bst = BinarySearchTreeMap()
        bst.insert(val, None)
        return bst
    else:
        bst = BinarySearchTreeMap()
        result_tup = helper(0, len(prefix_lst) - 1, 0)
        bst.root = result_tup[0]
        n_val = result_tup[1]
        bst.n = n_val

        return bst