"""
Problem Description
You are given a binary tree represented by root A. You need to check if it is a Binary Search Tree or not.
Assume a BST is defined as follows:
1) The left subtree of a node contains only nodes with keys less than the node's key.
2) The right subtree of a node contains only nodes with keys greater than the node's key.
3) Both the left and right subtrees must also be binary search trees.

Problem Constraints
1 <= Number of nodes in binary tree <= 105
0 <= node values <= 232-1

Input Format
First and only argument is head of the binary tree A.
Output Format
Return 0 if false and 1 if true.
Example Input 1:
   1
  /  \
 2    3
Input 2:
  2
 / \
1   3
Example Output 1: 0
Output 2: 1
"""
from binarytree import build


def solve(root):
    return is_bst(root, float('-inf'), float('inf'))


def is_bst(node, min_value, max_value):
    if node is None:
        return True
    if node.value <= min_value or node.value >= max_value:
        return False
    return is_bst(node.left, min_value, node.value) and is_bst(node.right, node.value, max_value)


if __name__ == '__main__':
    nodes = [7, 3, 15, 1, 5, 8, 20, 0, 2, 4, 6, None, None, 17, 26]
    root = build(nodes)
    print(root)
    print(solve(root))
    nodes = [1, 2, 3]
    root = build(nodes)
    print(root)
    print(solve(root))
