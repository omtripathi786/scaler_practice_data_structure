"""
Problem Description
Given a linked list of integers. Find and return the length
of the longest palindrome list that exists in that linked list.
A palindrome list is a list that reads the same backward and forward.
Expected memory complexity : O(1)

Problem Constraints
1 <= length of the linked list <= 2000
1 <= Node value <= 100

Input Format
The only argument given is head pointer of the linked list.
Output Format
Return the length of the longest palindrome list.
Example Input
1: 2 -> 3 -> 3 -> 3
Input 2: 2 -> 1 -> 2 -> 1 ->  2 -> 2 -> 1 -> 3 -> 2 -> 2
Example Output 1: 3
Output 2: 5

Example Explanation 1:
3 -> 3 -> 3 is largest palindromic sublist
Explanation 2:
2 -> 1 -> 2 -> 1 -> 2 is largest palindromic sublist.
"""
import linked_list as link


def longest_palindrome(head):
    dummy = link.Node(-1)
    curr = head
    prev = dummy
    ans = 0
    while curr:
        prevItr = prev
        nextItr = curr.next
        l = 1
        while prevItr and nextItr:
            if prevItr.value == nextItr.value:
                prevItr = prevItr.next
                nextItr = nextItr.next
                l += 1
            else:
                break
        ans = max(ans, l + l - 1)
        l = 0
        prevItr = prev
        nextItr = curr
        while prevItr and nextItr:
            if prevItr.value == nextItr.value:
                prevItr = prevItr.next
                nextItr = nextItr.next
                l += 1
            else:
                break
        ans = max(ans, 2 * l)
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return ans


if __name__ == "__main__":
    # 2 -> 1 -> 2 -> 1 ->  2 -> 2 -> 1 -> 3 -> 2 -> 2
    ll = link.create_ll([2, 1, 2, 1, 2, 2, 1, 3, 2, 2])
    print(longest_palindrome(ll.head))
