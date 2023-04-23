from LinkedBinaryTree import *

def create_expression_tree(prefix_exp_str):
    if not prefix_exp_str:
        return LinkedBinaryTree()
    
    prefix_lst = prefix_exp_str.split(" ")

    def create_expression_tree_helper(prefix_exp, start_pos):
        val = prefix_exp[start_pos]
        if val.isdigit():
            node1 = LinkedBinaryTree.Node(int(val))
            return (node1, 1)
        elif val in "+-*/":
            result1 = create_expression_tree_helper(prefix_exp, 1 + start_pos)
            if result1 is not None:
                left_tree = result1[0]
                left_pos = result1[1]
                result2 = create_expression_tree_helper(prefix_exp, 1 + start_pos + left_pos)
                if result2 is not None:
                    right_tree = result2[0]
                    right_pos = result2[1]
                    node1 = LinkedBinaryTree.Node(val, left_tree, right_tree)
                    return (node1, 1 + left_pos + right_pos)
    
    test = create_expression_tree_helper(prefix_lst, 0)
    return LinkedBinaryTree(test[0])


def prefix_to_postfix(prefix_exp_str):
    change = create_expression_tree(prefix_exp_str)
    result = list(change.postorder())
    return " ".join([str(node.data) for node in result])

prefix_exp_str = "- / 6 2 3"
tree = create_expression_tree(prefix_exp_str)
postfix_exp = prefix_to_postfix(prefix_exp_str)
print(postfix_exp)
