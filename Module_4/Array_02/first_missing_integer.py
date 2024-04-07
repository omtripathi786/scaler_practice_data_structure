"""
Problem Description
Given an unsorted integer array, A of size N. Find the first missing positive integer.
Note: Your algorithm should run in O(n) time and use constant space.

Problem Constraints
1 <= N <= 1000000
-109 <= A[i] <= 109

Input Format
First argument is an integer array A.

Output Format
Return an integer denoting the first missing positive integer.

Example Input
Input 1:
[1, 2, 0]
Input 2:
[3, 4, -1, 1]
Input 3:
[-8, -7, -6]
Example Output
Output 1:
3
Output 2:
2
Output 3:
1
"""


def first_missing_integer(arr):
    i = 0
    n = len(arr)
    while i < n:
        if 0 < arr[i] <= n:
            if arr[i] != i + 1:
                ind = arr[i] - 1
                if arr[i] != arr[ind]:
                    arr[i], arr[ind] = arr[ind], arr[i]
                    i -= 1
        i += 1

    for i in range(n):
        if arr[i] != i + 1:
            return i + 1
    return n + 1


if __name__ == '__main__':
    A = [1, 2, 0]
    print(first_missing_integer(A))
