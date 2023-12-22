"""
Problem Description
Given a singly linked list A: A0 → A1 → … → An-1 → An
reorder it to:
A0 → An → A1 → An-1 → A2 → An-2 → …
You must do this in-place without altering the nodes' values.

Problem Constraints
1 <= |A| <= 106

Input Format
The first and the only argument of input contains a pointer to the head of the linked list A.
Output Format
Return a pointer to the head of the modified linked list.

Example Input 1:
 A = [1, 2, 3, 4, 5]
Input 2:
 A = [1, 2, 3, 4]
Example Output
1:
[1, 5, 2, 4, 3]
Output 2:
[1, 4, 2, 3]
"""
import linked_list as ll


def reorder_list(A):
    # Find the middle of the linked list
    slow = fast = A
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # Reverse the second half of the linked list
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node
    # Merge the first and second half of the linked list
    first, second = A, prev
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next
    return A


if __name__ == '__main__':
    A = ll.create_ll([1, 2, 3, 4, 5])
    ll.LinkedList.print_ll(A.head)
    ans = reorder_list(A.head)
    ll.LinkedList.print_ll(ans)
