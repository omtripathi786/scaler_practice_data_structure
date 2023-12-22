"""
Problem Description
You are given two linked lists, A and B, representing two non-negative numbers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return it as a linked list.
Problem Constraints
1 <= |A|, |B| <= 105

Input Format
The first argument of input contains a pointer to the head of linked list A.
The second argument of input contains a pointer to the head of linked list B.

Output Format
Return a pointer to the head of the required linked list.

Example Input 1:
 A = [2, 4, 3]
 B = [5, 6, 4]
Input 2:
 A = [9, 9]
 B = [1]
Example Output 1:
 [7, 0, 8]
Output 2:
 [0, 0, 1]
Example
Explanation 1:
A = 342 and B = 465. A + B = 807.
Explanation 2:
A = 99 and B = 1. A + B = 100.
"""
import linked_list as ll


def add_two_numbers(A, B):
    dummy = ll.Node(0)
    current, carry = dummy, 0
    while A or B:
        sum = carry
        if A:
            sum += A.value
            A = A.next
        if B:
            sum += B.value
            B = B.next
        carry, value = divmod(sum, 10)
        current.next = ll.Node(value)
        current = current.next
    if carry != 0:
        current.next = ll.Node(carry)
    return dummy.next


if __name__ == '__main__':
    A = ll.create_ll([2, 4, 3])
    B = ll.create_ll([5, 6, 4])
    ll.LinkedList.print_ll(A.head)
    ll.LinkedList.print_ll(B.head)
    ans = add_two_numbers(A.head, B.head)
    ll.LinkedList.print_ll(ans)
