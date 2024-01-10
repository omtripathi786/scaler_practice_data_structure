"""
Problem Description
Given a binary tree, return a 2-D array with vertical order traversal of it.
Go through the example  for more details.

NOTE: If 2 Tree Nodes shares the same vertical level then the one with lesser depth will come first.

Problem Constraints
0 <= number of nodes <= 105

Input Format
First and only argument is a pointer to the root node of binary tree, A.
Output Format
Return a 2D array denoting the vertical order traversal of tree as shown.
Example Input 1:
      6
    /   \
   3     7
  / \     \
 2   5     9
Input 2:
      1
    /   \
   3     7
  /       \
 2         9
Example Output 1:
 [
    [2],
    [3],
    [6, 5],
    [7],
    [9]
 ]
Output 2:
 [
    [2],
    [3],
    [1],
    [7],
    [9]
 ]
"""
from binarytree import build


def vertical_order_traversal(root):
    queue = [(root, 0)]
    col_table = {}
    while queue:
        node, col = queue.pop(0)
        if col not in col_table:
            col_table[col] = []
        col_table[col].append(node.value)
        if node.left:
            queue.append((node.left, col - 1))
        if node.right:
            queue.append((node.right, col + 1))
    result = []
    for col in sorted(col_table.keys()):
        result.append(col_table[col])
    return result


if __name__ == '__main__':
    nodes = [6, 3, 7, 2, 5, None, 9]
    root = build(nodes)
    print(root)
    print(vertical_order_traversal(root))
