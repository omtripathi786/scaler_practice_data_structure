"""
Problem Description
You are given the head of a linked list A and an integer B,
check if there is any node which contains this value B.
Return 1 if such a node is present else return 0.

Problem Constraints
1 <= size of linked list <= 105
1 <= value of nodes <= 109
1 <= B <= 109

Input Format
The first argument A is the head of a linked list.
The second arguement B is an integer.
Output Format
Return 1 if such a node is present otherwise return 0.
Example Input
Input 1:
A = 1 -> 2 -> 3
B = 4
Input 2:
A = 4 -> 3 -> 2 -> 1
B = 4
Example Output
Output 1:
0
Output 2:
1
"""


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        current = A
        while current.next:
            if current.val == B:
                return 1
            current = current.next
        else:
            if current.val == B:
                return 1
            return 0
