"""
Problem Description
Given a Binary Search Tree(BST) A. If there is a node
with value B present in the tree delete it and return the tree.
Note - If there are multiple options, always replace a node by its in-order predecessor

Problem Constraints
2 <= No. of nodes in BST <= 105
1 <= value of nodes <= 109
Each node has a unique value

Input Format
The first argument is the root node of a Binary Search Tree A.
The second argument is the value B.
Output Format
Delete the given node if found and return the root of the BST.
Example Input 1:
            15
          /    \
        12      20
        / \    /  \
       10  14  16  27
      /
     8
     B = 10
Input 2:
            8
           / \
          6  21
         / \
        1   7
     B = 6
Example Output 1:
            15
          /    \
        12      20
        / \    /  \
       8  14  16  27
Output 2:
            8
           / \
          1  21
           \
            7
"""
from binarytree import build


def delete_node_in_bst(root, x):
    # if tree is empty return None
    if root is None:
        return None
    # if the value to be deleted is less than root call the method for left subtree
    if x < root.value:
        root.left = delete_node_in_bst(root.left, x)
    elif x > root.value:
        root.right = delete_node_in_bst(root.right, x)
    else:
        # if node to be deleted has no left child return the right child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # if node have both children find the maximum value in the left subtree
        # and replace node value with maximum node value and delete the maximum value from the left subtree
        temp = find_max(root.left)
        root.value = temp.value
        root.left = delete_node_in_bst(root.left, temp.value)
    return root


def find_max(node):
    curr = node
    while curr.right:
        curr = curr.right
    return curr


if __name__ == '__main__':
    nodes = [15, 12, 20, 10, 14, 16, 27, 8]
    root = build(nodes)
    print(root)
    bst = delete_node_in_bst(root,10)
    print(bst)
