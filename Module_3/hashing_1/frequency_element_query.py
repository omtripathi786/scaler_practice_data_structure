"""
Problem Description
Given an array A. You have some integers given in the array B.
For the i-th number, find the frequency of B[i] in the array A
and return a list containing all the frequencies.

Problem Constraints
1 <= |A| <= 105
1 <= |B| <= 105
1 <= A[i] <= 105
1 <= B[i] <= 105

Input Format
First argument A is an array of integers.
Second argument B is an array of integers denoting the queries.
Output Format
Return an array of integers containing frequency of the each element in B.
Example Input
Input 1:
A = [1, 2, 1, 1]
B = [1, 2]
Input 2:
A = [2, 5, 9, 2, 8]
B = [3, 2]
Example Output
Output 1:
[3, 1]
Output 2:
[0, 2]
"""


def solve(A, B):
    freq = {}
    for i in A:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    ans = []
    for i in B:
        if i in freq:
            ans.append(freq[i])
        else:
            ans.append(0)
    return ans


if __name__ == '__main__':
    A = [1, 2, 1, 1]
    B = [1, 2]
    print(solve(A, B))
