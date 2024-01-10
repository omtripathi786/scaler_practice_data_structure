"""
Problem Description
Given the inorder and postorder traversal of a tree, construct the binary tree.
NOTE: You may assume that duplicates do not exist in the tree.

Problem Constraints
1 <= number of nodes <= 105

Input Format
First argument is an integer array A denoting the inorder traversal of the tree.
Second argument is an integer array B denoting the postorder traversal of the tree.

Output Format
Return the root node of the binary tree.

Example Input 1:
 A = [2, 1, 3]
 B = [2, 3, 1]
Input 2:
 A = [6, 1, 3, 2]
 B = [6, 3, 2, 1]
Example Output 1:
   1
  / \
 2   3
Output 2:
   1
  / \
 6   2
    /
   3
"""
from binarytree import build, Node


def build_tree(A, B):
    if not A or not B:
        return None
    root = Node(B[-1])
    root_index = A.index(B[-1])
    root.left = build_tree(A[:root_index], B[:root_index])
    root.right = build_tree(A[root_index + 1:], B[root_index:-1])
    return root


if __name__ == '__main__':
    A = [6, 1, 3, 2]
    B = [6, 3, 2, 1]
    root = build_tree(A, B)
    print(root)
