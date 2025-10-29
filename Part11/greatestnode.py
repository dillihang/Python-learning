class Node:
    def __init__(self, value, left_child: "Node" = None, right_child: "Node" = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def print_nodes(root: Node):
    print(root.value)

    if root.left_child is not None:
        print_nodes(root.left_child)

    if root.right_child is not None:
        print_nodes(root.right_child)

def sum_of_nodes(root: Node):
    node_sum = root.value

    if root.left_child is not None:
        node_sum += sum_of_nodes(root.left_child)

    if root.right_child is not None:
        node_sum += sum_of_nodes(root.right_child)

    return node_sum

def greatest_node(root: "Node"):
    """
    Recursively finds the greatest value in a binary tree.

    The function traverses the tree starting from the root node, checking 
    each node's value and comparing it to the greatest value found in 
    its left and right subtrees.

    Args:
        root (Node): The root node of the binary tree.

    Returns:
        int: The greatest value present in the binary tree.
    """
    greatest_value = root.value

    if root.left_child is not None:
        left_greatest = greatest_node(root.left_child)
        if left_greatest > greatest_value:
            greatest_value = left_greatest
        
    if root.right_child is not None:
        right_greatest = greatest_node(root.right_child)
        if right_greatest > greatest_value:
            greatest_value = right_greatest
    
    return greatest_value


if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)

    # print(sum_of_nodes(tree))

    print(greatest_node(tree))
   
    