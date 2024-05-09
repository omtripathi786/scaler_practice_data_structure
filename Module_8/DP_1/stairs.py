"""
You are climbing a staircase, and it takes A steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Return the number of distinct ways modulo 1000000007

Problem Constraints
1 <= A <= 105

Input Format
The first and the only argument contains an integer A, the number of steps.

Output Format
Return an integer, representing the number of ways to reach the top.

Example Input 1:
 A = 2
Input 2:
 A = 3
Output 1:
 2
Output 2:
 3
Example Explanation 1:
 Distinct ways to reach top: [1, 1], [2].
Explanation 2:
 Distinct ways to reach top: [1 1 1], [1 2], [2 1].
"""


def stairs(n):
    ways = [0] * (n + 1)
    ways[0], ways[1] = 1, 1
    for i in range(2, n+1):
        ways[i] = (ways[i-1] + ways[i-2]) % 1000000007
    return ways[n]


if __name__ == '__main__':
    A = 3
    print(stairs(A))
