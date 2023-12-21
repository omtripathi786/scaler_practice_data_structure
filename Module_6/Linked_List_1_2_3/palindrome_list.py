"""
Problem Description
Given a singly linked list A, determine if it's a palindrome.
Return 1 or 0, denoting if it's a palindrome or not, respectively.

Problem Constraints
1 <= |A| <= 105
Input Format
The first and the only argument of input contains a pointer to the head of the given linked list.
Output Format
Return 0, if the linked list is not a palindrome.
Return 1, if the linked list is a palindrome.
Example Input 1:A = [1, 2, 2, 1]
Input 2:A = [1, 3, 2]
Example Output 1:1
Output 2:0
"""
import linked_list as link


def is_palindrome(head):
    # find the middle of the linked list
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # reverse the second half
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    # compare the first half and reversed second half
    while prev:
        if prev.value != head.value:
            return 0
        prev = prev.next
        head = head.next
    return 1


if __name__ == '__main__':
    ll1 = link.create_ll([1, 2, 2, 1])
    ll2 = link.create_ll([1, 3, 2])
    ll1.print_ll(ll1.head)
    print(is_palindrome(ll2.head))
