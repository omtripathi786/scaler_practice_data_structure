"""
Problem Description
Given an array A of N integers. Construct prefix sum of the array in the given array itself.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 103

Input Format
Only argument A is an array of integers.

Output Format
Return an array of integers denoting the prefix sum of the given array.

Example Input
Input 1:
A = [1, 2, 3, 4, 5]
Example Output
Output 1:
[1, 3, 6, 10, 15]
"""


def solve(A):
    for i in range(1, len(A)):
        A[i] = A[i] + A[i - 1]
    return A


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    print(solve(A))
