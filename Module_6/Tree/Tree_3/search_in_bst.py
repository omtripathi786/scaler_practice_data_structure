"""
Problem Description
Given a Binary Search Tree A. Check whether there exists a node with value B in the BST.

Problem Constraints
1 <= Number of nodes in binary tree <= 105
0 <= B <= 106

Input Format
First argument is a root node of the binary tree, A.
Second argument is an integer B.

Output Format
Return 1 if such a node exist and 0 otherwise
Example Input 1:
            15
          /    \
        12      20
        / \    /  \
       10  14  16  27
      /
     8

     B = 16
Input 2:
            8
           / \
          6  21
         / \
        1   7
     B = 9
Example Output 1:1
Output 2:0
"""
from binarytree import build


def search(root, x):
    curr = root
    while curr:
        if curr.value == x:
            return curr.value
        elif x > curr.value:
            curr = curr.right
        else:
            curr = curr.left
    return 'No Match'


if __name__ == "__main__":
    nodes = [7, 3, 15, 1, 5, 8, 20, 0, 2, 4, 6, None, None, 17, 26]
    root = build(nodes)
    print(root)
    print(search(root, 8))
