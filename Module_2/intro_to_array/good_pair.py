"""
Problem Description:-
Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B).
Check if any good pair exist or not.

Problem Constraints
1 <= A.size() <= 104
1 <= A[i] <= 109
1 <= B <= 109

Input Format
First argument is an integer array A.
Second argument is an integer B.
Output Format
Return 1 if good pair exist otherwise return 0.
"""


def solve(A):
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == B:
                return 1
    else:
        return 0


if __name__ == '__main__':
    print(solve([5, 5, 3]))
