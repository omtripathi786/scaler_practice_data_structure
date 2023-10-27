"""
Problem Description
Given an integer array A containing N distinct integers, you have to find all the leaders in array A.
An element is a leader if it is strictly greater than all the elements to its right side.
NOTE: The rightmost element is always a leader.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 108

Input Format
There is a single input argument which a integer array A
Output Format
Return an integer array denoting all the leader elements of the array.
Example Input
Input 1:
 A = [16, 17, 4, 3, 5, 2]
Input 2:
 A = [5, 4]
Example Output
Output 1:
[17, 2, 5]
Output 2:
[5, 4]
"""


def brute_force(A):
    """
    Time Complexity O(N^2)
    :param A:
    :return: Leader Array
    """
    lead_arr = [A[-1]]
    for i in range(len(A) - 1):
        is_lead = True
        for j in range(i + 1, len(A) - 1):
            if A[j] >= A[i]:
                is_lead = False
                break
        else:
            if is_lead:
                lead_arr.append(A[i])
    return lead_arr


def solve(A):
    """
    Time Complexity O(N)
    :param A:
    :return: Leader Array
    """
    lead_arr = [A[-1]]
    max_el = A[-1]
    for i in range((len(A)-2), -1, -1):
        if A[i] >= max_el:
            max_el = A[i]
            lead_arr.append(A[i])
    return lead_arr


if __name__ == '__main__':
    A = [16, 17, 4, 3, 5, 2]
    print(brute_force(A))
    print(solve(A))
