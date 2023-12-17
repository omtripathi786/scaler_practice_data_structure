"""
Note:- this program can not be tested by just simply running it.
as I have not written the linked list class and test cases.

Problem Description
You are given A which is the head of a linked list. Also given is the
value B and position C. Complete the function that should insert a new
node with the said value at the given position.

Notes:
In case the position is more than length of linked list, simply insert the new node at the tail only.
In case the pos is 0, simply insert the new node at head only.
Follow 0-based indexing for the node numbering.

Problem Constraints
0 <= size of linked list <= 105
1 <= value of nodes <= 109
1 <= B <= 109
0 <= C <= 105

Input Format
The first argument A is the head of a linked list.
The second argument B is an integer which denotes the value of the new node
The third argument C is an integer which denotes the position of the new node

Output Format
Return the head of the linked list

Example Input
Input 1:
A = 1 -> 2
B = 3
C = 0
Input 2:
A = 1 -> 2
B = 3
C = 1
Example Output
Output 1:
3 -> 1 -> 2
Output 2:
1 -> 3 -> 2
"""
from linked_list import Node


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def solve(self, A, B, C):
        new_node = Node(B)
        if C == 0 or A is None:
            new_node.next = A
            return new_node
        count = 0
        current = A
        while current.next and count <= C - 1:
            count += 1
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return A
