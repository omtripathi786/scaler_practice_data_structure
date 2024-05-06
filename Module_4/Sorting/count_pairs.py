"""
Given two array A and B of size M and N, find the number of pairs of such that
A[i] > B[j]
"""


def count_pairs_merge_array(A, B):
    A.sort()
    B.sort()
    m, n = len(A), len(B)
    pairs = 0
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
            pairs += m - i
    while i < m:
        ans[k] = A[i]
        i += 1
        k += 1
    while j < n:
        ans[k] = B[j]
        j += 1
        k += 1

    return ans, pairs


if __name__ == '__main__':
    A = [7, 3, 5]
    B = [2, 0, 6]
    print(count_pairs_merge_array(A,B))
