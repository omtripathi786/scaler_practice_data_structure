"""
Problem Description
Merge two sorted linked lists, A and B, and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists and should also be sorted.

Problem Constraints
0 <= |A|, |B| <= 105
Input Format
The first argument of input contains a pointer to the head of linked list A.
The second argument of input contains a pointer to the head of linked list B.
Output Format
Return a pointer to the head of the merged linked list.
Example Input 1:
A = 5 -> 8 -> 20
B = 4 -> 11 -> 15
Input 2:
A = 1 -> 2 -> 3
B = Null
Example Output 1: 4 -> 5 -> 8 -> 11 -> 15 -> 20
Output 2:   1 -> 2 -> 3
"""
import linked_list as ll


def merge_sorted_ll(head1, head2):
    dummy = ll.Node(0)
    curr = dummy
    while head1 and head2:
        if head1.value < head2.value:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next
    if head1:
        curr.next = head1
    if head2:
        curr.next = head2
    return dummy.next


if __name__ == '__main__':
    A = ll.create_ll([5, 8, 20])
    B = ll.create_ll([4, 11, 15])
    A.print_ll(A.head)
    B.print_ll(B.head)
    ans = merge_sorted_ll(A.head, B.head)
    ll.LinkedList.print_ll(ans)
