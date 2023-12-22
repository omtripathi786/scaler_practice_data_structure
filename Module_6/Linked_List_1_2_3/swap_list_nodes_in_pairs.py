"""
Problem Description
Given a linked list A, swap every two adjacent nodes and return its head.
NOTE: Your algorithm should use only constant space. You may not modify the values in the list;
only nodes themselves can be changed.

Problem Constraints
1 <= |A| <= 106

Input Format
The first and the only argument of input contains a pointer to the head of the given linked list.

Output Format
Return a pointer to the head of the modified linked list.

Example Input 1:
 A = 1 -> 2 -> 3 -> 4
Input 2:
 A = 7 -> 2 -> 1
Example Output 1:
 2 -> 1 -> 4 -> 3
Output 2:
 2 -> 7 -> 1
"""
import linked_list as ll


def swap_list_nodes(head):
    dummy = ll.Node(0)
    dummy.next = head
    current = dummy
    while current.next and current.next.next:
        first = current.next
        second = current.next.next
        first.next = second.next
        current.next = second
        current.next.next = first
        current = current.next.next
    return dummy.next


if __name__ == '__main__':
    ll1 = ll.create_ll([1, 2, 3, 4])
    ll.LinkedList.print_ll(ll1.head)
