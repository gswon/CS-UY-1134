from LinkedBinaryTree import *

def is_height_balanced(bin_tree):
    def height_val(bin_root):
        if bin_root is None:
            return (0, True)
        else:
            left_root = height_val(bin_root.left)
            right_root = height_val(bin_root.right)
            check1 = max(left_root[0], right_root[0]) + 1
            check2 = left_root[1] and right_root[1]
            val = left_root[0] - right_root[0]
            if abs(val) <= 1:
                return (check1, check2)
            else:
                check2 = False
                return (check1, check2)
        
    if bin_tree.root is None:
        return True
    elif bin_tree.root.left is None and bin_tree.root.right is None:
        return True
    else:
        return height_val(bin_tree.root)[1]
    
# test0 - when tree contains nothing
# a = LinkedBinaryTree()
# print(is_height_balanced(a))

# test1
# a = LinkedBinaryTree.Node(0)
# # b = LinkedBinaryTree.Node(1)

# # c = LinkedBinaryTree.Node(1, a, b)
# # d = LinkedBinaryTree.Node(2, c)

# # e = LinkedBinaryTree.Node(3)
# # f = LinkedBinaryTree.Node(4)

# # g = LinkedBinaryTree.Node(5, e, f)
# # h = LinkedBinaryTree.Node(6, d, g)

# # bin_tree = LinkedBinaryTree(h)
# print(is_height_balanced(a))

#test2
# a1 = LinkedBinaryTree(LinkedBinaryTree.Node(1))
# print(is_height_balanced(a1))

# #test3
# a2 = LinkedBinaryTree.Node(2)
# b2 = LinkedBinaryTree.Node(3, a2, None)
# bin_tree = LinkedBinaryTree(b2)
# print(is_height_balanced(bin_tree))