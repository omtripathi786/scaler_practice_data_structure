"""
Problem Description
Given an array of integers A and an integer B, find and return the maximum value
K such that there is no subarray in A of size K with the sum of elements greater than B.

Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 10^9
1 <= B <= 10^9

Input Format
The first argument given is the integer array A.
The second argument given is integer B.

Output Format
Return the maximum value of K (sub array length).

Example Input 1:
A = [1, 2, 3, 4, 5]
B = 10
Input 2:
A = [5, 17, 100, 11]
B = 130
Example Output 1:
 2
Output 2:
 3
"""


def special_integer(A, B):
    n = len(A)
    prefix_sum = [0] * n
    for i in range(n):
        if i == 0:
            prefix_sum[i] = A[i]
        else:
            prefix_sum[i] = prefix_sum[i - 1] + A[i]
    low, high = 1, n
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        max_sum = max([prefix_sum[i + mid - 1] - (prefix_sum[i - 1] if i > 0 else 0) for i in range(n - mid + 1)])
        if max_sum <= B:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans


if __name__ == '__main__':
    A = [5, 17, 100, 11]
    B = 130
    print(special_integer(A, B))
