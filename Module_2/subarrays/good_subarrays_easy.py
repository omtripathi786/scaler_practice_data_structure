"""
Problem Description
Given an array of integers A, a subarray of an array is said to be good if
it fulfills any one of the criteria:
1. Length of the subarray is be even, and the sum of all the
elements of the subarray must be less than B.
2. Length of the subarray is be odd, and the sum of all the elements
of the subarray must be greater than B.
Your task is to find the count of good subarrays in A.

Problem Constraints
1 <= len(A) <= 103
1 <= A[i] <= 103
1 <= B <= 107

Input Format
The first argument given is the integer array A.
The second argument given is an integer B.
Output Format
Return the count of good subarrays in A.
Example Input
Input 1:
A = [1, 2, 3, 4, 5]
B = 4
Input 2:
A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
B = 65
Example Output
Output 1:
6
Output 2:
36
"""


def solve(A, B):
    n = len(A)
    pref = [0] * (n)
    pref[0] = A[0]
    for i in range(1, n):
        pref[i] = pref[i - 1] + A[i]
    ans = 0
    for i in range(n):
        for j in range(i, n):
            sum = pref[j]
            if i == 0:
                sum = pref[j]
            else:
                sum = pref[j] - pref[i - 1]
            sz = j - i + 1
            if sz % 2 == 0 and sum < B: ans += 1
            if sz % 2 != 0 and sum > B: ans += 1
    return ans


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    B = 4
    print(solve(A, B))
