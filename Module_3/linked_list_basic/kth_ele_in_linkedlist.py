"""
Note:- this program can not be tested by just simply running it.
as I have not written the linked list class and test cases.

Problem Description
You are given the head of a linked list A and an integer B.
You need to find the B-th element of the linked list and return its value.
Note : Follow 0-based indexing for the node numbering.

Problem Constraints
1 <= size of linked list <= 105
1 <= value of nodes <= 109
0 <= B < size of linked list

Input Format
The first argument A is the head of a linked list.
The second arguement B is an integer.
Output Format
Return an integer.

Example Input
Input 1:
A = 1 -> 2 -> 3
B = 0
Input 2:
A = 4 -> 3 -> 2 -> 1
B = 1
Example
Output 1:
1
Output 2:
3
"""


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if B == 0:
            return A.val
        current = A
        count = 0
        while count < B - 1 and current.next:
            count += 1
            current = current.next
        return current.next.val
