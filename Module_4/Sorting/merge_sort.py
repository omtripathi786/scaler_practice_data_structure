def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    m, n = len(left), len(right)
    i, j, k = 0, 0, 0
    merged = [0] * (m + n)
    while i < m and j < n:
        if left[i] < right[j]:
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
        k += 1

    while i < m:
        merged[k] = left[i]
        i += 1
        k += 1

    while j < n:
        merged[k] = right[j]
        j += 1
        k += 1
    return merged


if __name__ == '__main__':
    A = [3, 2, 6, 1, 9, 7, 7]
    print(merge_sort(A))
