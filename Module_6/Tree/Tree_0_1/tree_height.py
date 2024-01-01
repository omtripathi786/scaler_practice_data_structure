"""
Problem Description
You are given the root node of a binary tree A. You have to find the height of the given tree.
A binary tree's height is the number of nodes along the longest path from the root node down to the farthest leaf node.

Problem Constraints
1 <= Number of nodes in the tree <= 105
0 <= Value of each node <= 109
Input Format
The first and only argument is a tree node A.
Output Format
Return an integer denoting the height of the tree.

Example Input 1:
 Values =  1
          / \
         4   3
Input 2:
 Values =  1
          / \
         4   3
        /
       2

Example Output 1: 2
Output 2: 3
"""
from binarytree import build


def height(root):
    if root is None:
        return 0
    l = height(root.left)
    r = height(root.right)
    return max(l, r) + 1


def count_node(root):
    if root is None:
        return 0
    l = count_node(root.left)
    r = count_node(root.right)
    return l + r + 1


if __name__ == '__main__':
    nodes = [1, 4, 3, 2]
    binary_tree = build(nodes)
    print(binary_tree)
    print(height(binary_tree))
    print(count_node(binary_tree))
