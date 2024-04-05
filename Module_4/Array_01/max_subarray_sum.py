"""
Problem Description
Find the maximum sum of contiguous non-empty subarray within an array A of length N.

Problem Constraints
1 <= N <= 1e6
-1000 <= A[i] <= 1000

Input Format
The first and the only argument contains an integer array, A.
Output Format
Return an integer representing the maximum possible sum of the contiguous subarray.
Example Input 1:A = [1, 2, 3, 4, -10]
Input 2: A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Example Output 1: 10
Output 2: 6
"""


def max_subarray_sum(A):
    ans = float('-inf')
    subarray_sum = 0
    for i in range(len(A)):
        subarray_sum += A[i]
        ans = max(ans, subarray_sum)
        if subarray_sum < 0:
            subarray_sum = 0
    return ans


def max_subarray(A):
    ans = float('-inf')
    subarray_sum = 0
    start = -1
    end = -1
    s = 0
    for e in range(len(A)):
        subarray_sum += A[e]
        if subarray_sum > ans:
            ans = subarray_sum
            start = s
            end = e
        if subarray_sum < 0:
            subarray_sum = 0
            s = e + 1
    return A[start:end + 1]


if __name__ == '__main__':
    A = [1, 2, 3, 4, -10, -2]
    B = [-2, 1, -3, 4, -1, 2, 1, -5]
    print(max_subarray_sum(A))
    print(max_subarray_sum(B))
    print(max_subarray(B))
