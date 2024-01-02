"""
Problem Description
Given a binary tree, return the Postorder traversal of its nodes values.

Problem Constraints
1 <= number of nodes <= 105

Input Format
First and only argument is root node of the binary tree, A.

Output Format
Return an integer array denoting the Postorder traversal of the given binary tree.
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
Example Output 1:[3, 2, 1]
Output 2:[6, 3, 2, 1]
"""
from binarytree import build


def postorder_traversal(root, ans=None):
    # left, right, node (L, R, N)
    if ans is None:
        ans = []
    if root is not None:
        postorder_traversal(root.left, ans)
        postorder_traversal(root.right, ans)
        ans.append(root.value)
    return ans


def iterative_traversal(root):
    # left, right, node (L, R, N)
    stack = [root]
    ans = []
    while stack:
        node = stack.pop()
        ans.append(node.value)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return ans[::-1]


if __name__ == '__main__':
    nodes = [1, 6, 2, None, None, 3]
    binary_tree = build(nodes)
    print(binary_tree)
    print(postorder_traversal(binary_tree))
    print(iterative_traversal(binary_tree))
