"""
Problem Description
Given an array A of length N, return the subarray from B to C.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109
0 <= B <= C < N

Input Format
The first argument A is an array of integers
The remaining argument B and C are integers.

Output Format
Return a subarray
Example Input
Input 1:
A = [4, 3, 2, 6]
B = 1
C = 3
Input 2:
A = [4, 2, 2]
B = 0
C = 1
Example Output
Output 1:
[3, 2, 6]
Output 2:
[4, 2]
"""


def brute_force(A, B, C):
    n = len(A)
    ans = []
    for i in range(B, C + 1):
        ans.append(A[i])

    return ans


if __name__ == '__main__':
    A = [4, 3, 2, 6]
    B = 1
    C = 3
    print(brute_force(A, B, C))
