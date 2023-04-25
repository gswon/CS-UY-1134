from ArrayQueue import ArrayQueue

class LinkedBinaryTree:

    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.count_nodes()

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0


    def count_nodes(self):
        def subtree_count(root):
            if (root is None):
                return 0
            else:
                left_count = subtree_count(root.left)
                right_count = subtree_count(root.right)
                return 1 + left_count + right_count

        return subtree_count(self.root)


    def sum(self):
        def subtree_sum(root):
            if (root is None):
                return 0
            else:
                left_sum = subtree_sum(root.left)
                right_sum = subtree_sum(root.right)
                return root.data + left_sum + right_sum

        return subtree_sum(self.root)


    def height(self):
        def subtree_height(root):
            if (root.left is None and root.right is None):
                return 0
            elif (root.left is None):
                return 1 + subtree_height(root.right)
            elif (root.right is None):
                return 1 + subtree_height(root.left)
            else:
                left_height = subtree_height(root.left)
                right_height = subtree_height(root.right)
                return 1 + max(left_height, right_height)

        if(self.is_empty()):
            raise Exception("Tree is empty")
        return subtree_height(self.root)


    def preorder(self):
        def subtree_preorder(root):
            if (root is None):
                pass
            else:
                yield root
                yield from subtree_preorder(root.left)
                yield from subtree_preorder(root.right)

        yield from subtree_preorder(self.root)


    def postorder(self):
        def subtree_postorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_postorder(root.left)
                yield from subtree_postorder(root.right)
                yield root

        yield from subtree_postorder(self.root)


    def inorder(self):
        def subtree_inorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)


    def breadth_first(self):
        if (self.is_empty()):
            return
        line = ArrayQueue()
        line.enqueue(self.root)
        while (line.is_empty() == False):
            curr_node = line.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                line.enqueue(curr_node.left)
            if (curr_node.right is not None):
                line.enqueue(curr_node.right)

    def __iter__(self):
        for node in self.breadth_first():
            yield node.data
            
    def iterative_inorder_version2(self):
        if self.is_empty():
            return
        
        curr = self.root

        while curr.left is not None:
            curr = curr.left

        check = None

        while curr is not None:
            if check == curr.left:
                yield curr.data
                check = curr
                if curr.right is not None:
                    curr = curr.right
                else:
                    curr = curr.parent
            elif check == curr.right:
                check = curr
                curr = curr.parent
            else:
                if curr.left is None:
                    yield curr.data
                    check = curr
                    if curr.right is None:
                        curr = curr.parent
                    else:
                        curr = curr.right
                else:
                    curr = curr.left


    def iterative_inorder(self):
        if self.is_empty():
            raise Exception("Empty Tree")
        elif len(self) == 1:
            yield self.root.data
            return
        
        curr = self.root
        prev = None

        while curr is not None:
            if curr.left is None:
                yield curr.data
                curr = curr.right
            else:
                prev = curr.left
                while (prev.right is not None) and (prev.right is not curr):
                    prev = prev.right
                if prev.right is None:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    yield curr.data
                    curr = curr.right

a = LinkedBinaryTree.Node(5)
b = LinkedBinaryTree.Node(1)

c = LinkedBinaryTree.Node(9, None, b)
d = LinkedBinaryTree.Node(2, c)

e = LinkedBinaryTree.Node(8)
f = LinkedBinaryTree.Node(4)

g = LinkedBinaryTree.Node(7, e, f)
h = LinkedBinaryTree.Node(3, d, g)

bin_tree = LinkedBinaryTree(h)
for item in bin_tree.iterative_inorder():
    print(item, end= ' ')
print()        
