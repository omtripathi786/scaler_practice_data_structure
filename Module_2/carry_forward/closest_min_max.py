"""
Problem Description
Given an array A, find the size of the smallest subarray such that it contains
at least one occurrence of the maximum value of the array and at least one
occurrence of the minimum value of the array.

Problem Constraints
1 <= |A| <= 2000

Input Format
First and only argument is vector A
Output Format
Return the length of the smallest subarray which has at least one occurrence
of minimum and maximum element of the array

Example Input
Input 1:
A = [1, 3, 2]
Input 2:
A = [2, 6, 1, 6, 9]
Example Output
Output 1:
 2
Output 2:
 3
"""


def brute_force(A):
    """
    Time Complexity O(N^2)
    Space Complexity O(1)
    :param A:
    :return: len_min
    """
    max_e, min_e = max(A), min(A)
    len_min = len(A)
    for s in range(len(A)):
        for e in range(s, len(A)):
            # print(A[s:e+1])
            if (A[s] == min_e and A[e] == max_e) or (A[s] == max_e and A[e] == min_e):
                l = ((e - s) + 1)
                len_min = min(l, len_min)
    return len_min


def solve(A):
    """
    Time Complexity O(N^2)
    Space Complexity O(1)
    :param A:
    :return: len_min
    """
    min_idx = -1
    max_idx = -1
    max_e, min_e = max(A), min(A)
    len_min = len(A)
    for i in range(len(A)):
        if A[i] == max_e:
            if min_idx != -1:
                l = i - min_idx + 1
                len_min = min(len_min, l)
            max_idx = i
        if A[i] == min_e:
            if max_idx != -1:
                l = i - max_idx + 1
                len_min = min(len_min, l)
            min_idx = i

    return len_min


if __name__ == '__main__':
    A = [2, 6, 1, 6, 9]
    # print(brute_force(A))
    print(solve(A))
