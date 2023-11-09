"""
Problem Description
You are given an integer array C of size A. Now you need to find a subarray
 (contiguous elements) so that the sum of contiguous elements is maximum.
But the sum must not exceed B.

Problem Constraints
1 <= A <= 103
1 <= B <= 109
1 <= C[i] <= 106

Input Format
The first argument is the integer A.
The second argument is the integer B.
The third argument is the integer array C.
Output Format
Return a single integer which denotes the maximum sum.
Example Input
Input 1:
A = 5
B = 12
C = [2, 1, 3, 4, 5]
Input 2:
A = 3
B = 1
C = [2, 2, 2]

Example Output
Output 1:
12
Output 2:
0
"""


def brute_force(A, B, C):
    p = [0] * A
    for i in range(A):
        if i == 0:
            p[i] = C[i]
        else:
            p[i] = p[i - 1] + C[i]
    ans = []
    for s in range(A):
        for e in range(s, A):
            if s == 0 and p[e] <= B:
                ans.append(p[e])
            elif (p[e] - p[s - 1]) <= B:
                ans.append(p[e] - p[s - 1])

    return max(ans)


if __name__ == '__main__':
    A = 9
    B = 76
    C = [9, 5, 7, 8, 10, 1, 8, 3, 2]
    print(brute_force(A, B, C))
