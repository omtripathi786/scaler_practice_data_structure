"""
Problem Description
Given a binary tree A. Check whether it is possible to partition the tree to two
trees which have equal sum of values after removing exactly one edge on the original tree.

Problem Constraints
1 <= size of tree <= 100000
0 <= value of node <= 109

Input Format
First and only argument is head of tree A.
Output Format
Return 1 if the tree can be partitioned into two trees of equal sum else return 0.
Example Input 1:
                5
               /  \
              3    7
             / \  / \
            4  6  5  6
Input 2:
                1
               / \
              2   10
                  / \
                 20  2
Example Output 1:  1
Output 2:   0
"""
from binarytree import build


def tree_sum(node, total_sum=None):
    if node is None:
        return 0
    return node.value + tree_sum(node.left) + tree_sum(node.right)


def solution(root_node):
    total = tree_sum(root_node)
    if total % 2 != 0:
        return 0
    half = total / 2
    ans = False

    def subtree_sum(node):
        nonlocal ans
        if node is None:
            return 0
        l = subtree_sum(node.left)
        r = subtree_sum(node.right)
        node_sum = node.value + l + r
        if node_sum == half:
            ans = True
        return node_sum
    subtree_sum(root_node)
    return ans


if __name__ == "__main__":
    nodes = [5, 3, 7, 4, 6, 5, 6]
    root = build(nodes)
    print(root)
    print(solution(root))
