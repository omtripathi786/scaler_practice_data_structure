"""
Problem Description
Given a sorted array of integers A where every element appears twice
except for one element which appears once, find and return this single element that appears only once.
Elements which are appearing twice are adjacent to each other.
NOTE: Users are expected to solve this in O(log(N)) time.

Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 10^9

Input Format
The only argument given is the integer array A.
Output Format
Return the single element that appears only once.
Example Input
Input 1:
A = [1, 1, 7]
Input 2:
A = [2, 3, 3]
Example Output
Output 1:
 7
Output 2:
 2
"""


def solve(A):
    n = len(A)
    left, right = 0, n - 1
    while left <= right:
        m = (left + right) // 2
        if (A[m] == 0 or A[m] != A[m - 1]) and (m != n - 1 or A[m] != A[m + 1]):
            return A[m]
        if A[m] == A[m - 1]:
            ti = m - 1
        else:
            ti = m

        if ti % 2 == 0:
            left = m + 1
        else:
            right = m - 1


if __name__ == '__main__':
    A = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 11, 11, 12, 12]
    print(solve(A))
