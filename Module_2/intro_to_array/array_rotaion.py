"""
given an integer array A of size N and an integer B, you have to return the same array after rotating it
B Problem Description
Gtimes towards the right.

Input Format
The first argument given is the integer array A.
The second argument given is the integer B.

Output Format
Return the array A after rotating it B times to the right

"""


def solve(A, B):
    N = len(A)
    effective_rotations = B % N
    rotated_array = [0] * N
    for i in range(N):
        rotated_array[(i + effective_rotations) % N] = A[i]
    return rotated_array


if __name__ == '__main__':
    A = [1, 2, 3, 4]
    B = 2
    print(solve(A, B))
