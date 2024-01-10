"""
Problem Description
Given a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Problem Constraints
1 <= number of nodes <= 105

Input Format
First and only argument is root node of the binary tree, A.

Output Format
Return a 2D integer array denoting the level order traversal of the given binary tree.

Example Input 1:
    3
   / \
  9  20
    /  \
   15   7
Input 2:
   1
  / \
 6   2
    /
   3
Example Output 1:

 [
   [3],
   [9, 20],
   [15, 7]
 ]
Output 2:

 [
   [1]
   [6, 2]
   [3]
 ]
Example Explanation 1:
 Return the 2D array. Each row denotes the traversal of each level.
"""
from binarytree import build
from collections import deque


def level_order(root):
    queue = [root]
    ans = []
    while queue:
        node = queue.pop(0)
        ans.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return ans


def level_order2(root):
    queue = [root]
    result = []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


if __name__ == '__main__':
    nodes = [1, 2, 3, 5, 8, 10, 13, 6, None, None, None, 9, 7,
             4, None, None, None, None, None, None, None, None, None, None, None, 12, 11]
    root = build(nodes)
    print(root)
    print(level_order(root))
    print(level_order2(root))
