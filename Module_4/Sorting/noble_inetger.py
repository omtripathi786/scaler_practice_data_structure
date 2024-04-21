"""
Problem Description
Given an integer array A, find if an integer p exists in the array such that the number of
integers greater than p in the array equals p.

Problem Constraints
1 <= |A| <= 2*105
-108 <= A[i] <= 108
Input Format
First and only argument is an integer array A.
Output Format
Return 1 if any such integer p is present else, return -1.

Example Input 1:
 A = [3, 2, 1, 3]
Input 2:
 A = [1, 1, 3, 3]
Example Output 1:
 1
Output 2:
 -1
"""


def noble_integer(A):
    A.sort()
    n = len(A)
    for i in range(n - 1):
        if A[i] == A[i + 1]:
            continue
        if A[i] == n - i - 1:
            return 1
    if A[n - 1] == 0:
        return 1
    return -1


if __name__ == '__main__':
    A = [3, 2, 1, 3]
    print(noble_integer(A))
