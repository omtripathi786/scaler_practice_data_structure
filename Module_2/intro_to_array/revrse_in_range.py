"""
Problem Description
Given an array A of N integers. Also given are two integers B and C. Reverse the array A in the given range [B, C]

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109
0 <= B <= C <= N - 1

Input Format
The first argument A is an array of integer.
The second and third arguments are integers B and C

Output Format
Return the array A after reversing in the given range
"""


def solve(A, B, C):
    i, j = B, C
    while i < j:
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
        i += 1
        j -= 1
    return A


if __name__ == '__main__':
    A = [1, 2, 3, 4]
    B = 0
    C = 3
    print(solve(A, B, C))
