"""
Problem Description
You are given a singly linked list having head node A.
You have to reverse the linked list and return the head node of that reversed list.
NOTE: You have to do it in-place and in one-pass.

Problem Constraints
1 <= Length of linked list <= 105
Value of each node is within the range of a 32-bit integer.
Input Format
First and only argument is a linked-list node A.
Output Format
Return a linked-list node denoting the head of the reversed linked list.
Example Input 1: A = 1 -> 2 -> 3 -> 4 -> 5 -> NULL
Input 2: A = 3 -> NULL
Example Output 1: 5 -> 4 -> 3 -> 2 -> 1 -> NULL
Output 2: 3 -> NULL
"""
import linked_list as link


def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


if __name__ == '__main__':
    ll = link.create_ll([1, 2, 3, 4, 5, 6, 7, 8])
    ll.print_ll(ll.head)
    rll = reverse_linked_list(ll.head)
    ll.print_ll(rll)
