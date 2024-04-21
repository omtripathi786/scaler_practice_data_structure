def merge_sort(A, left, right):
    if left == right:
        return
    mid = (left + right) // 2
    merge_sort(A, left, mid)
    merge_sort(A, mid + 1, right)
    A[left:right + 1] = merge_two_sorted_array(A[left:mid + 1], A[mid + 1:right + 1])
    return A


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
    A = [3, 2, 6, 1, 9, 7, 7]
    print(merge_sort(A, 0, len(A)))
