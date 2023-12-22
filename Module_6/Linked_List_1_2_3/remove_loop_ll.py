"""
Problem Description
You are given a linked list that contains a loop.
You need to find the node, which creates a loop and break it by making the node point to NULL.

Problem Constraints
1 <= number of nodes <= 1000

Input Format
The first of the input contains a LinkedList, where the first number is the number of nodes N,
and the next N nodes are the node value of the linked list.
The second line of the input contains an integer which denotes the position of node where cycle starts.

Output Format
return the head of the updated linked list.
Example Input 1:
1 -> 2
^    |
| - -
Input 2:
3 -> 2 -> 4 -> 5 -> 6
          ^         |
          |         |
          - - - - - -
Example Output 1:  1 -> 2 -> NULL
Output 2:   3 -> 2 -> 4 -> 5 -> 6 -> NULL
"""
import linked_list as ll


def delete_loop(head):
    slow = fast = head
    # Detect the loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    # if no loop detected return rhe same head
    if not fast or not fast.next:
        return head

    # find the cycle of the loop and break the cycle
    slow = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next
    fast.next = None
    return head


if __name__ == '__main__':
    ll1 = ll.create_cyclic_ll([3, 2, 4, 5, 6], 2)
    ll.LinkedList.print_cyclic_ll(ll1.head)
    ans = delete_loop(ll1.head)
    ll.LinkedList.print_ll(ans)
