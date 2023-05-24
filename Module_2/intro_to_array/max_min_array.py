"""
Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.
Problem Constraints
1 <= N <= 105
-109 <= A[i] <= 109

Input Format
First argument A is an integer array.

Output Format
Return the sum of maximum and minimum element of the array
"""


def solve(A):
    max_ele = A[0]
    min_ele = A[0]
    for i in A:
        if i > max_ele:
            max_ele = i
        elif i < min_ele:
            min_ele = i
    return max_ele + min_ele


if __name__ == '__main__':
    A = [-2, 1, -4, 5, 3]
    print(solve(A))
