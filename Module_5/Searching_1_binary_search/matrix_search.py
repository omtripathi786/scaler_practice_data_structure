"""
Problem Description
Given a matrix of integers A of size N x M and an integer B.
Write an efficient algorithm that searches for integer B in matrix A.
This matrix A has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Return 1 if B is present in A, else return 0.
NOTE: Rows are numbered from top to bottom, and columns are from left to right.

Problem Constraints
1 <= N, M <= 1000
1 <= A[i][j], B <= 106

Input Format
The first argument given is the integer matrix A.
The second argument given is the integer B.

Output Format
Return 1 if B is present in A else, return 0.

Example Input
Input 1:
A = [
      [1,   3,  5,  7]
      [10, 11, 16, 20]
      [23, 30, 34, 50]
    ]
B = 3
Input 2:
A = [
      [5, 17, 100, 111]
      [119, 120, 127, 131]
    ]
B = 3
Example Output
Output 1: 1
Output 2: 0
"""


def binary_search(A, B):
    n = len(A)
    left, right = 0, n - 1
    while left <= right:
        m = (left + right) // 2
        if A[m] == B:
            return True
        if B > A[m]:
            left = m + 1
        else:
            right = m - 1
    else:
        return False


def solve(A, B):
    ans = 0
    for matrix in A:
        if binary_search(matrix, B):
            ans = 1
    return ans


if __name__ == '__main__':
    A = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    B = 3
    print(solve(A, B))
