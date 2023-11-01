"""
Problem Description
Given an array A of N integers, return the number of unique elements in the array.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109

Input Format
First argument A is an array of integers.
Output Format
Return an integer.
Example Input
Input 1:
A = [3, 4, 3, 6, 6]
Input 2:
A = [3, 3, 3, 9, 0, 1, 0]
Example Output
Output 1:
3
Output 2:
4
"""


def solve(A):
    B = set()
    for i in A:
        B.add(i)
    return len(B)


if __name__ == '__main__':
    A = [4, -1, 1]
    print(solve(A))
