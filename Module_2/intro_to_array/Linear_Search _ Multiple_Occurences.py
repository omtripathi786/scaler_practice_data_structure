"""
Given an array A and an integer B, find the number of occurrences of B in A.
Problem Constraints

1 <= B, Ai <= 109
1 <= |A| <= 105

Input Format
Given an integer array A and an integer B.

Output Format
Return an integer, number of occurrences of B in A.
"""


def solve(A, B):
    count = 0
    for i in A:
        if i == B:
            count += 1
    return count


if __name__ == '__main__':
    A = [1, 2, 2]
    B = 2
    print(solve(A, B))
