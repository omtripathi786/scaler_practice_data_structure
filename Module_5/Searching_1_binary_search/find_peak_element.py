"""
Problem Description
Given an array of integers A, find and return the peak element in it.
An array element is considered a peak if it is not smaller than its neighbors.
For corner elements, we need to consider only one neighbor.
NOTE:
It is guaranteed that the array contains only a single peak element.
Users are expected to solve this in O(log(N)) time. The array may contain duplicate elements.

Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 109

Input Format
The only argument given is the integer array A.
Output Format
Return the peak element.
Example Input
Input 1: A = [1, 2, 3, 4, 5]
Input 2: A = [5, 17, 100, 11]
Example Output
Output 1: 5
Output 2: 100
"""


def solve(A):
    n = len(A)
    left, right = 0, n - 1
    while left <= right:
        m = (left + right) // 2
        if (A[m] == 0 or A[m] > A[m - 1]) and (m == n - 1 or A[m] > A[m + 1]):
            return A[m]

        if A[m] == 0 or A[m] > A[m - 1]:
            left = m + 1
        else:
            right = m - 1
    else:
        return False


if __name__ == '__main__':
    A = [5, 17, 100, 11]
    print(solve(A))
