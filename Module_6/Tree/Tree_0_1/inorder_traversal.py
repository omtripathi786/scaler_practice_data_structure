"""
Problem Description
Given a binary tree, return the inorder traversal of its nodes' values.

Problem Constraints
1 <= number of nodes <= 105
Input Format
First and only argument is root node of the binary tree, A.
Output Format
Return an integer array denoting the inorder traversal of the given binary tree.
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
Example Output 1:[1, 3, 2]
Output 2: [6, 1, 3, 2]
"""
from binarytree import build


def inorder_traversal(root, ans=None):
    # left, node, right (L, N, R)
    if ans is None:
        ans = []
    if root is not None:
        inorder_traversal(root.left, ans)
        ans.append(root.value)
        inorder_traversal(root.right, ans)
    return ans


if __name__ == '__main__':
    nodes = [1, 6, 2, None, None, 3]
    binary_tree = build(nodes)
    print(binary_tree)
    print(inorder_traversal(binary_tree))
