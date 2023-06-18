"""
Problem Description
You are given an integer array A of length N.
You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
For each query, you have to find the sum of all elements from L to R indices in A (0 - indexed).
More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.

Problem Constraints
1 <= N, M <= 105
1 <= A[i] <= 109
0 <= L <= R < N

Input Format
The first argument is the integer array A.
The second argument is the 2D integer array B.

Output Format
Return an integer array of length M where ith element is the answer for ith query in B.

Example Input
Input 1:
A = [1, 2, 3, 4, 5]
B = [[0, 3], [1, 2]]
Input 2:

A = [2, 2, 2]
B = [[0, 0], [1, 2]]


Example Output
Output 1:
[10, 5]
Output 2:

[2, 4]
"""


def solve(A, B):
    psum = [0] * len(A)
    for i in range(len(A)):
        if i == 0:
            psum[i] = A[i]
        else:
            psum[i] = psum[i - 1] + A[i]
    result = []
    for query in B:
        s, e = query
        q_sum = 0
        if s == 0:
            q_sum = psum[e]
        else:
            q_sum = psum[e] - psum[s - 1]
        result.append(q_sum)

    return result


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    B = [[0, 3], [1, 2]]
    print(solve(A, B))
