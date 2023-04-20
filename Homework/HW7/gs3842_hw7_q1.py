from LinkedBinaryTree import *

def min_and_max(bin_tree): 
    def subtree_min_and_max(root):
        if root.left is None and root.right is None:
            return (root.data, root.data)
        elif root.left is None:
            right_root = subtree_min_and_max(root.right)
            return (min(right_root[0], root.data), max(right_root[1], root.data))
        elif root.right is None:
            left_root = subtree_min_and_max(root.left)
            return (min(left_root[0], root.data), max(left_root[1], root.data))
        else:
            left_root = subtree_min_and_max(root.left)
            right_root = subtree_min_and_max(root.right)
            return (min(left_root[0], right_root[0], root.data), max(left_root[1], right_root[1], root.data))   
    if bin_tree.root is None:
        raise Exception("Tree is Empty")
    else:    
        return subtree_min_and_max(bin_tree.root)
    
a = LinkedBinaryTree(LinkedBinaryTree.Node(1))
print(min_and_max(a))