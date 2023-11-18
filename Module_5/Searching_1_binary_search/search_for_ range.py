"""
Problem Description
Given a sorted array of integers A (0-indexed) of size N,
find the left most and the right most index of a given integer B in the array A.
Return an array of size 2, such that
          First element = Left most index of B in A
          Second element = Right most index of B in A.
If B is not found in A, return [-1, -1].
Note : Your algorithm's runtime complexity must be in the order of O(log n).

Problem Constraints
1 <= N <= 106
1 <= A[i], B <= 109

Input Format
The first argument given is the integer array A.
The second argument given is the integer B.
Output Format
Return the left most and right most index (0-based) of B in A as
a 2-element array. If B is not found in A, return [-1, -1].
Example Input
Input 1:
A = [5, 7, 7, 8, 8, 10]
B = 8
Input 2:
A = [5, 17, 100, 111]
B = 3
Example Output
Output 1:[3, 4]
Output 2:[-1, -1]
"""


def solve(A, B):
    n = len(A)
    left, right = 0, n - 1
    first_o = -1
    while left <= right:
        m = (left + right) // 2
        if A[m] == B:
            first_o = m
            right = m - 1
        elif B > A[m]:
            left = m + 1
        else:
            right = m - 1
    if first_o == -1:
        return [-1, -1]
    left, right = first_o, n - 1
    second_o = -1
    while left <= right:
        m = (left + right) // 2
        if A[m] == B:
            second_o = m
            left = m + 1
        elif B > A[m]:
            left = m + 1
        else:
            right = m -1
    return [first_o, second_o]


if __name__ == '__main__':
    A = [5, 7, 7, 8, 8, 10]
    B = 8
    print(solve(A, B))
