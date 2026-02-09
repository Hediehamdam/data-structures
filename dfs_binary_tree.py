"""
File Name: dfs_binary_tree.py
Description: Implements DFS traversal (preorder, inorder, postorder) on a Binary Tree.
Data Structure/Algorithm: Binary Tree, Depth First Search (DFS)
Operations: preorder, inorder, postorder
Use Case: Tree traversal, practicing DFS, foundation for advanced algorithms
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")

if __name__ == "__main__":
    # Example tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Preorder traversal:")
    preorder(root)
    print("\nInorder traversal:")
    inorder(root)
    print("\nPostorder traversal:")
    postorder(root)
