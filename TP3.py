# TP3 Exercise

def build_adjacency_matrix(edges, num_nodes):
    matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]

    for edge in edges:
        start, end = edge
        if 1 <= start <= num_nodes and 1 <= end <= num_nodes:
            matrix[start - 1][end - 1] = 1  
        else:
            print(f"Invalid edge: {edge}")

    return matrix


edges_list = [
    (1, 2), (1, 3), (2, 5), (2, 6),
    (3, 4), (4, 8), (5, 7)
]
nodes_count = 8

adj_matrix = build_adjacency_matrix(edges_list, nodes_count)

print("a) Adjacency Matrix for the given graph:")
for line in adj_matrix:
    print(line)


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

# Perform inorder traversal of a binary tree
def traverse_inorder(node):
    if node is None:
        return

    traverse_inorder(node.left_child)
    print(node.value, end=" ")
    traverse_inorder(node.right_child)

# Search for a node with the given value in the binary tree
def search_subtree(root, target):
    if root is None:
        return None

    if root.value == target:
        return root

    left_search = search_subtree(root.left_child, target)
    if left_search:
        return left_search
    return search_subtree(root.right_child, target)


if __name__ == "__main__":
    tree_root = BinaryTreeNode(1)

    tree_root.left_child = BinaryTreeNode(3)
    tree_root.left_child.left_child = BinaryTreeNode(4)
    tree_root.left_child.left_child.left_child = BinaryTreeNode(8)

    tree_root.right_child = BinaryTreeNode(2)
    tree_root.right_child.left_child = BinaryTreeNode(6)
    tree_root.right_child.right_child = BinaryTreeNode(5)
    tree_root.right_child.right_child.left_child = BinaryTreeNode(7)

    x = int(input("b) Inorder Traversal: Enter the root value of the subtree to traverse: "))

    subtree = search_subtree(tree_root, x)
    if subtree:
        print(f"Inorder traversal of subtree rooted at node {x}:")
        traverse_inorder(subtree)
    else:
        print(f"Node number {x} not found in the tree.")
