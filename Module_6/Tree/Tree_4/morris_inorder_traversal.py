"""
Problem Description
Given a binary tree, return the inorder traversal of its nodes' values.

NOTE: Using recursion and stack are not allowed.

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
Output 2:[6, 1, 3, 2]
    ______7__
       /         \
    __3__         15___
   /     \       /     \
  1       5     8      _20
 / \     / \          /   \
0   2   4   6        17    26

"""


def morris_inorder_traversal(root):
    curr = root
    ans = []
    while curr is not None:
        if curr.left is None:
            ans.append(curr.value)
            curr = curr.right
        else:
            pre = curr.left
            while pre.right is not None and pre.right != curr:
                pre = pre.right
            if pre.right is None:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                ans.append(curr.value)
                curr = curr.right
    return ans


from binarytree import build

if __name__ == "__main__":
    nodes = [7, 3, 15, 1, 5, 8, 20, 0, 2, 4, 6, None, None, 17, 26]
    root = build(nodes)
    print(root)
    print(morris_inorder_traversal(root))
