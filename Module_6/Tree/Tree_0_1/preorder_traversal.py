"""
Problem Description
Given a binary tree, return the preorder traversal of its nodes values.

Problem Constraints
1 <= number of nodes <= 105

Input Format
First and only argument is root node of the binary tree, A.
Output Format
Return an integer array denoting the preorder traversal of the given binary tree.
Example Input 1:
   1
    \
     2
    /
   3
Input 2:
   1
  / \
 6   2
    /
   3

Example Output 1: [1, 2, 3]
Output 2: [1, 6, 2, 3]
"""
from binarytree import build


def preorder_traversal(root, ans=None):
    if ans is None:
        ans = []
    if root is not None:
        ans.append(root.value)
        preorder_traversal(root.left, ans)
        preorder_traversal(root.right, ans)
    return ans


if __name__ == '__main__':
    nodes = [1, 6, 2, None, None, 3]
    binary_tree = build(nodes)
    print(binary_tree)
    print(preorder_traversal(binary_tree))
