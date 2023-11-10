"""
Problem Description
You are given a N X N integer matrix. You have to find the sum of
all the minor diagonal elements of A.
Minor diagonal of a M X M matrix A is a collection of elements A[i, j]
such that i + j = M + 1 (where i, j are 1-based).

Problem Constraints
1 <= N <= 103
-1000 <= A[i][j] <= 1000

Input Format
First and only argument is a 2D integer matrix A.
Output Format
Return an integer denoting the sum of minor diagonal elements.
Example Input
Input 1:
 A = [[1, -2, -3],
      [-4, 5, -6],
      [-7, -8, 9]]
Input 2:
 A = [[3, 2],
      [2, 3]]
"""


def solve(A):
    n = len(A)
    i, j = 0, n - 1
    dsum = 0
    while i < n and j >= 0:
        dsum += A[i][j]
        i += 1
        j -= 1
    return dsum


if __name__ == '__main__':
    A = [
        [1, 2, 3],
        [5, 6, 7],
        [9, 2, 3]
    ]
    print(solve(A))
