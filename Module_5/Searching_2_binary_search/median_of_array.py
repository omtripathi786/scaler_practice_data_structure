"""
Problem Description
There are two sorted arrays A and B of sizes N and M respectively.
Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).
NOTE:
The overall run time complexity should be O(log(m+n)).
IF the number of elements in the merged array is even, then the
median is the average of (n/2)th and (n/2+1)th element. For example,
if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5.

Problem Constraints
1 <= N + M <= 2*106

Input Format
The first argument is an integer array A of size N.
The second argument is an integer array B of size M.

Output Format
Return a decimal value denoting the median of two sorted arrays.

Example Input
Input 1:
 A = [1, 4, 5]
 B = [2, 3]
Input 2:
 A = [1, 2, 3]
 B = [4]
Example Output
Output 1: 3.0
Output 2: 2.5
"""


def brute_force(A, B):
    C = []  # merged array
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    # remaining element of A
    while i < len(A):
        C.append(A[i])
        i += 1
    # remaining element of B
    while j < len(B):
        C.append(B[j])
        j += 1

    n = len(C)
    if n % 2 == 0:
        mid1 = C[(n // 2) - 1]
        mid2 = C[(n // 2)]
        return (mid1 + mid2) / 2
    else:
        return C[n // 2]


def solve(A, B):
    if len(A) > len(B):
        return solve(B, A)
    m, n = len(A), len(B)
    low, high = 0, m
    while low <= high:
        cut1 = (low + high) // 2
        cut2 = (m + n) // 2 - cut1

        l1 = float('-inf') if cut1 == 0 else A[cut1 - 1]
        l2 = float('-inf') if cut2 == 0 else B[cut2 - 1]
        r1 = float('inf') if cut1 == m else A[cut1]
        r2 = float('inf') if cut2 == n else B[cut2]

        if l1 <= r2 and l2 <= r1:
            if (m + n) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2
            else:
                return min(r1, r2)
        elif l1 > r2:
            high = cut1 - 1
        else:
            low = cut1 + 1


if __name__ == '__main__':
    A = [-50, -41, -40, -19, 5, 21, 28]
    B = [-50, -21, -10]
    print(solve(A, B))
