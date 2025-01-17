"""
Problem Description
You are given a 2D integer matrix A, return a 1D integer array containing row-wise sums of original matrix.

Problem Constraints
1 <= A.size() <= 103
1 <= A[i].size() <= 103
1 <= A[i][j] <= 103

Input Format
First argument is a 2D array of integers.(2D matrix).
Output Format
Return an array containing column-wise sums of original matrix.
Example Input
Input 1:
[1,2,3,4]
[5,6,7,8]
[9,2,3,4]

Example Output
Output 1:
[10,26,18]
"""


def solve(A):
    row = len(A)
    col = len(A[0])
    ans = []
    for i in range(row):
        row_sum = 0
        for j in range(col):
            row_sum += A[i][j]
        ans.append(row_sum)

    return ans


if __name__ == '__main__':
    A = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 2, 3, 4]
    ]
    print(solve(A))
