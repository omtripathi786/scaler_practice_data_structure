"""
Problem Description
You have given a string A having Uppercase English letters.
You have to find the number of pairs (i, j) such that A[i] = 'A', A[j] = 'G' and i < j.

Problem Constraints
1 <= length(A) <= 105

Input Format
First and only argument is a string A.

Output Format
Return an long integer denoting the answer.

Example Input
Input 1:
 A = "ABCGAG"
Input 2:
 A = "GAB"
Example Output
Output 1:
 3
Output 2:
 0
"""


def brute_force(A):
    count = 0
    for i in range(len(A)):
        if A[i] == 'A':
            for j in range(i + 1, len(A)):
                if A[j] == 'G':
                    count += 1
    return count


def solve(A):
    count = 0
    ans = 0
    for i in range(len(A)):
        if A[i] == 'A':
            count += 1
        elif A[i] == 'G':
            ans += count
    return ans


if __name__ == '__main__':
    A = "ABCGAG"
    print(brute_force(A))
    print(solve(A))
