"""
Problem Description
Given two sorted integer arrays A and B, merge B and A as one sorted array and return it as an output.
Note: A linear time complexity is expected and you should avoid use of any library function.

Problem Constraints
-2×109 <= A[i], B[i] <= 2×109
1 <= |A|, |B| <= 5×104
Input Format
First Argument is a 1-D array representing  A.
Second Argument is also a 1-D array representing B.

Output Format
Return a 1-D vector which you got after merging A and B.

Example Input
1:
A = [4, 7, 9]
B = [2, 11, 19]
Input 2:
A = [1]
B = [2]
Example Output
1:
[2, 4, 7, 9, 11, 19]
Output 2:
[1, 2]
"""


def merge_two_sorted_array(A, B):
    m, n = len(A), len(B)
    i, j, k = 0, 0, 0
    ans = [0] * (m + n)
    while i < m and j < n:
        if A[i] <= B[j]:
            ans[k] = A[i]
            i += 1
            k += 1
        else:
            ans[k] = B[j]
            k += 1
            j += 1
    while i < m:
        ans[k] = A[i]
        i += 1
        k += 1
    while j < n:
        ans[k] = B[j]
        j += 1
        k += 1

    return ans


if __name__ == '__main__':
    A = [4, 7, 9]
    B = [2, 11, 19]
    print(merge_two_sorted_array(A, B))
