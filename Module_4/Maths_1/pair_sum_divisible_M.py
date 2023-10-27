"""
Problem Description
Given an array of integers A and an integer B, find and return the number of pairs in A whose sum is divisible by B.
Since the answer may be large, return the answer modulo (109 + 7).
Note: Ensure to handle integer overflow when performing the calculations.

Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 109
1 <= B <= 106

Input Format
The first argument given is the integer array A.
The second argument given is the integer B.

Output Format
Return the total number of pairs for which the sum is divisible by B modulo (109 + 7).

Example Input
Input 1:
 A = [1, 2, 3, 4, 5]
 B = 2

Example Output
Output 1:
 4
"""


def brute_force(A, B):
    count = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            pair_sum = A[i] + A[j]
            if pair_sum % B == 0:
                count += 1
    return count


def solve(A, B):
    n = len(A)
    hash_map = {}
    for i in range(n):
        if A[i] % B not in hash_map:
            hash_map[A[i] % B] = 1
        else:
            hash_map[A[i] % B] += 1
    ans = 0
    for i in range(n-1, -1, -1):
        rema = A[i] % B
        if rema == 0:
            remb = 0
        else:
            remb = B - rema
        ans += hash_map[remb]
        hash_map[rema] += 1
    return ans


if __name__ == '__main__':
    A = [5, 17, 100, 11]
    B = 28
    #A = [2, 3, 4, 8, 16, 15, 5, 12, 7, 18, 10, 9, 16, 21]
    #B = 6
    # print(brute_force(A, B))
    print(solve(A, B))
