"""
Problem Description
Given a binary search tree represented by root A, write a function to find the Bth smallest element in the tree.

Problem Constraints
1 <= Number of nodes in binary tree <= 100000
0 <= node values <= 10^9

Input Format
First and only argument is head of the binary tree A.

Output Format
Return an integer, representing the Bth element.

Example Input 1:
            2
          /   \
         1    3
B = 2
Input 2:
            3
           /
          2
         /
        1
B = 1
Example Output 1: 2
Output 2: 1

"""
from binarytree import build


def kth_smallest(root, B):
    cnt, ans = 0, None
    cnt, ans = inorder(root, B, cnt, ans)
    return ans


def inorder(root, B, cnt, ans):
    if root:
        cnt, ans = inorder(root.left, B, cnt, ans)
        cnt += 1
        if cnt == B:
            ans = root.val
            return cnt, ans
        if cnt < B:
            cnt, ans = inorder(root.right, B, cnt, ans)
    return cnt, ans


if __name__ == "__main__":
    nodes = [7, 3, 15, 1, 5, 8, 20, 0, 2, 4, 6, None, None, 17, 26]
    root = build(nodes)
    print(root)
    print(kth_smallest(root, 1))
