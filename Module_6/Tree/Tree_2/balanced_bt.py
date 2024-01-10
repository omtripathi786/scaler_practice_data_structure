"""
Problem Description
Given a root of binary tree A, determine if it is height-balanced.
A height-balanced binary tree is defined as a binary tree in which the depth of
the two subtrees of every node never differ by more than 1.

Problem Constraints
1 <= size of tree <= 100000

Input Format
First and only argument is the root of the tree A.
Output Format
Return 0 / 1 ( 0 for false, 1 for true ) for this problem.

Example Input 1:
    1
   / \
  2   3
Input 2:
       1
      /
     2
    /
   3
Example Output 1: 1
Output 2: 0
"""
from binarytree import build


def height(root):
    if root is None:
        return 0
    l = height(root.left)
    r = height(root.right)
    return max(l, r) + 1


def is_balanced(root):
    if root is None:
        return True
    lsh = height(root.left)
    rsh = height(root.right)
    if abs(lsh - rsh) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)


def is_balanced_tree(root):
    if check_height(root) == -1:
        return False
    else:
        return True


def check_height(root):
    if root is None:
        return 0
    lsh = check_height(root.left)
    if lsh == -1:
        return -1
    rsh = check_height(root.right)
    if rsh == -1:
        return -1
    diff = abs(lsh - rsh)
    if diff > 1:
        return -1
    else:
        return max(lsh, rsh) + 1


if __name__ == '__main__':
    nodes = [1, 2, 3, 5, 8, 10, 13, 6, None, None, None, 9, 7,
             4, None, None, None, None, None, None, None, None, None, None, None, 12, 11]
    # nodes = [1,2,None,3]
    root = build(nodes)
    print(root)
    print(is_balanced(root))
    print(is_balanced_tree(root))
