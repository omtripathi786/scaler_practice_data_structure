"""
Problem Description
You are given a n x n 2D matrix A representing an image.
Rotate the image by 90 degrees (clockwise).
You need to do this in place.
Note: If you end up using an additional array, you will only receive partial score.

Problem Constraints
1 <= n <= 1000

Input Format
First argument is a 2D matrix A of integers
Output Format
Return the 2D rotated matrix.
Example Input
Input 1:
 [
    [1, 2],
    [3, 4]
 ]
Input 2:
 [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
 ]
Example Output
Output 1:
 [
    [3, 1],
    [4, 2]
 ]
Output 2:
 [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
 ]
"""


def solve(A):
    n = len(A)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            A[i][j], A[j][i] = A[j][i], A[i][j]

    # Reverse each row to get the clockwise rotation
    for i in range(n):
        A[i].reverse()

    return A


if __name__ == '__main__':
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(solve(A))
