"""
Problem Description:-
You are given a constant array A.
You are required to return another array which is the reversed form of the input array.

Problem Constraints
1 <= A.size() <= 10000
1 <= A[i] <= 10000

Input Format
First argument is a constant array A.

Output Format
Return an integer array.
"""


def solve(A):
    i = 0
    j = len(A) - 1
    ans = [0] * len(A)
    while i <= j:
        ans[i] = A[j]
        ans[j] = A[i]
        i += 1
        j -= 1
    return ans


if __name__ == '__main__':
    A = [1, 2, 3, 4]
    print(solve(A))
