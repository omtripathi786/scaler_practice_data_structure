"""
Problem Description
Given an array of integers A and an integer B.
Find the total number of subarrays having sum equals to B.

Problem Constraints
 1 <= length of the array <= 50000
-1000 <= A[i] <= 1000

Input Format
The first argument given is the integer array A.
The second argument given is integer B.

Output Format
Return the total number of subarrays having sum equals to B.
Example Input
Input 1:
A = [1, 0, 1]
B = 1
Input 2:
A = [0, 0, 0]
B = 0
Example Output
Output 1:
4
Output 2:
6
Example Explanation
Explanation 1:
[1], [1, 0], [0, 1] and [1] are four subarrays having sum 1.
Explanation 1:
All the possible subarrays having sum 0.
"""


def brute_force(A, B):
    """

    :param A: integer array
    :param B: integer
    :return: number of subarray sum equal to B
    """
    n = len(A)
    psum = [0] * n
    for i in range(n):
        if i == 0:
            psum[i] = A[i]
        else:
            psum[i] = psum[i - 1] + A[i]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if psum[j] - psum[i] == B:
                count += 1
        if A[i] == B:
            count += 1
    return count


def solve(A, B):
    n = len(A)
    psum = [0] * n
    for i in range(n):
        if i == 0:
            psum[i] = A[i]
        else:
            psum[i] = psum[i - 1] + A[i]
    s = set()
    count = 0
    for i in range(n):
        if A[i] == B:
            count += 1
        if A[i] - B in s:
            count += 1
        s.add(A[i])

    return count


if __name__ == '__main__':
    A = [1, 0, 1]
    B = 1
    print(solve(A, B))
