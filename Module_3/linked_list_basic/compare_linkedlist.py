"""
Note:- this program can not be tested by just simply running it.
as I have not written the linked list class and test cases.

Problem Description
Given heads of two linked lists A and B, check if they are identical i.e.
each of their corresponding nodes should contain the same data. The two
given linked lists may or may not be of the same length.

Problem Constraints
1 <= size of linked lists <= 105
1 <= value of each node <= 109

Input Format
You are given the head of two linked lists A and B.
Output Format
Return 1 if both the linked lists are identical and 0 otherwise
Example Input
Input 1:
A = 1 -> 2 -> 3
B = 1 -> 2 -> 3
Input 2:
A = 4 -> 3 -> 2 -> 1
B = 4 -> 2 -> 3 -> 1
Example Output
Output 1:
1
Output 2:
0
"""


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return an integer
    def solve(self, A, B):
        curr_1 = A
        curr_2 = B
        while curr_1 or curr_2:
            if not curr_1 or not curr_2 or curr_1.val != curr_2.val:
                return 0
            curr_1 = curr_1.next if curr_1 else None
            curr_2 = curr_2.next if curr_2 else None

        return 1
