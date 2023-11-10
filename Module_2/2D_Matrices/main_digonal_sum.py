"""
Problem Description
You are given a N X N integer matrix. You have to find the
sum of all the main diagonal elements of A.


Problem Constraints
1 <= N <= 103
-1000 <= A[i][j] <= 1000
Input Format
There are 1 lines in the input. First 2 integers R, C are the number of rows and columns.
Then R * C integers follow corresponding to the rowwise numbers in the 2D array A.

Output Format
Return an integer denoting the sum of main diagonal elements.
"""


def solve(A):
    n = len(A)
    dsum = 0
    for i in range(n):
        # i == j for all diagonal
        dsum += A[i][i]
    return dsum


if __name__ == '__main__':
    A = [
        [1, 2, 3],
        [5, 6, 7],
        [9, 2, 3]
    ]
    print(solve(A))
