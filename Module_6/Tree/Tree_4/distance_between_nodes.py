"""
Problem Description
Given a binary search tree.
Return the distance between two nodes with given two keys B and C. It may be assumed that both keys exist in BST.
NOTE: Distance between two nodes is number of edges between them.

Problem Constraints
1 <= Number of nodes in binary tree <= 1000000
0 <= node values <= 109

Input Format
First argument is a root node of the binary tree, A.
Second argument is an integer B.
Third argument is an integer C.

Output Format
Return an integer denoting the distance between two nodes with given two keys B and C

Example Input 1:

         5
       /   \
      2     8
     / \   / \
    1   4 6   11
 B = 2
 C = 11
Input 2:

         6
       /   \
      2     9
     / \   / \
    1   4 7   10
 B = 2
 C = 6

Example Output 1: 3
Output 2: 1
"""
from binarytree import build


def distance_from_root(root_node, x):
    if root_node is None:
        return 0
    if x < root_node.val:
        return 1 + distance_from_root(root_node.left, x)
    else:
        return 1 + distance_from_root(root_node.right, x)


def distanceBetween2(root_node, x, y):
    if root_node is None:
        return 0
    if x < root_node.value and y < root_node.value:
        return distanceBetween2(root_node.left, x, y)
    if x > root_node.value and y > root_node.value:
        return distanceBetween2(root_node.right, x, y)
    if x <= root_node.value and y <= root_node.value:
        return distance_from_root(root_node,x)


def solve(node, x, y):
    if x > y:
        x, y = y, x
    return distanceBetween2(node, x, y)


if __name__ == '__main__':
    nodes = [5, 2, 8, 1, 4, 6, 11]
    root = build(nodes)
    print(root)
    print(solve(root, 2, 11))
