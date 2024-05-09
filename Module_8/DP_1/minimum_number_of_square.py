"""
Problem Description
Given an integer A. Return minimum count of numbers, sum of whose squares is equal to A.

Problem Constraints
1 <= A <= 105

Input Format
First and only argument is an integer A.

Output Format
Return an integer denoting the minimum count.

Example Input 1:
 A = 6
Input 2:
 A = 5
Example Output 1:
 3
Output 2:
 2
Example Explanation 1:

 Possible combinations are : (12 + 12 + 12 + 12 + 12 + 12) and (12 + 12 + 22).
 Minimum count of numbers, sum of whose squares is 6 is 3.
Explanation 2:

 We can represent 5 using only 2 numbers i.e. 12 + 22 = 5
"""
import sys

import sys
import math

sys.setrecursionlimit(10600)


def minimum_number_of_square(n):
    dp = [-1] * (n + 1)
    dp[0] = 0

    def _helper(n):
        if dp[n] != -1:
            return dp[n]
        i = 1
        min_val = float("inf")
        while i * i <= n:
            min_val = min(min_val, _helper(n - (i * i)))
            i += 1
        dp[n] = min_val + 1
        return dp[n]

    return _helper(n)


def iterative_approach(n):
    dp = [0] + [float('inf')] * n
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(1, int(math.sqrt(i)) + 1):
            dp[i] = min(dp[i], dp[i - (j * j)] + 1)
    return dp[n]


def iterative_approach1(n):
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        min_val = float("inf")
        j = 1
        while j * j <= n:
            min_val = min(min_val, abs(dp[i - (j * j)]))
            j += 1
        dp[i] = min_val + 1
    return dp[n]


if __name__ == '__main__':
    A = 6
    print(minimum_number_of_square(A))
    print(iterative_approach(A))
    print(iterative_approach1(A))
