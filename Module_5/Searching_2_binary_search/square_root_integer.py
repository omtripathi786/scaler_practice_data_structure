"""
Problem Description
Given an integer A. Compute and return the square root of A.
If A is not a perfect square, return floor(sqrt(A)).

NOTE:
The value of A*A can cross the range of Integer.
Do not use the sqrt function from the standard library.
Users are expected to solve this in O(log(A)) time.

Problem Constraints
0 <= A <= 109

Input Format
The first and only argument given is the integer A.
Output Format
Return floor(sqrt(A))
Example Input 1:11
Input 2:9
Example Output 1:3
Output 2:3
"""


def solve(A):
    if A == 0 or A == 1:
        return A
    low, high = 1, A
    ans = 0
    while low <= high:
        m = (low + high) // 2
        if m * m == A:
            return m
        elif m * m < A:
            ans = m
            low = m + 1
        else:
            high = m - 1
    return ans


if __name__ == '__main__':
    A = 11
    print(solve(A))
