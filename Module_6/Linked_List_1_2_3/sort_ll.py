"""
Problem Description
Sort a linked list, A in O(n log n) time.

Problem Constraints
0 <= |A| = 105
Input Format
The first and the only argument of input contains a pointer to the head of the linked list, A.
Output Format
Return a pointer to the head of the sorted linked list.
Example Input 1:
A = [3, 4, 2, 8]
Input 2:
A = [1]
Example Output 1: [2, 3, 4, 8]
Output 2:[1]
"""
import linked_list as ll
import merge_sorted_ll as merge


def sort_ll(head):
    if head is None or head.next is None:
        return head
    mid = find_middle_element(head)
    next_to_mid = mid.next
    mid.next = None
    left = sort_ll(head)
    right = sort_ll(next_to_mid)
    sorted_list = merge.merge_sorted_ll(left, right)
    return sorted_list


def find_middle_element(head):
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == '__main__':
    ll_1 = ll.create_ll([3, 4, 2, 8])
    ll.LinkedList.print_ll(ll_1.head)
    ll.LinkedList.print_ll(sort_ll(ll_1.head))
