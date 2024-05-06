"""
Problem Description
Given a sorted array of integers A of size N and an integer B,
where array A is rotated at some pivot unknown beforehand.
For example, the array [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2].
Your task is to search for the target value B in the array. If found, return its index; otherwise, return -1.
You can assume that no duplicates exist in the array.
NOTE: You are expected to solve this problem with a time complexity of O(log(N)).

Problem Constraints
1 <= N <= 1000000
1 <= A[i] <= 109
All elements in A are Distinct.

Input Format
The First argument given is the integer array A.
The Second argument given is the integer B.
Output Format
Return index of B in array A, otherwise return -1
Example Input
Input 1:
A = [4, 5, 6, 7, 0, 1, 2, 3]
B = 4
Input 2:
A : [ 9, 10, 3, 5, 6, 8 ]
B : 5
Example Output 1: 0
Output 2: 3
"""


def solve(A, B):
    n = len(A)
    low, high = 0, n - 1
    while low <= high:
        m = (low + high) // 2
        # case 1:- B is found at the middle
        if A[m] == B:
            return m
        # case 2:- left half is sorted
        if A[low] <= A[m]:
            if A[low] <= B < A[m]:
                high = m - 1
            else:
                low = m + 1
        # case 3:- right half is sorted
        else:
            if A[m] < B <= A[high]:
                low = m + 1
            else:
                high = m - 1
    return -1


if __name__ == '__main__':
    A = [4, 5, 6, 7, 0, 1, 2, 3]
    B = 4
    print(solve(A, B))
