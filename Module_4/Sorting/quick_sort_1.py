"""
Given an integer array consider 1st element as pivot.
rearrange the elements such that for all i
if A[i] < p then it should present on the left side
if A[i] > p then it should present on the right side

Note :- all elements are distinct

A = [54, 26, 93, 17, 77, 31, 44, 55, 20]
ans = [17, 20, 26, 31, 44, 54, 55, 77, 93]
"""


def partition_array(arr, start, end):
    pivot = arr[start]
    i = start + 1
    j = end
    while i <= j:
        if arr[i] < pivot:
            i += 1
        elif arr[j] > pivot:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    arr[start], arr[j] = arr[j], arr[start]
    return j


def quick_sort(arr, start, end):
    if start >= end:
        return arr
    pivot = partition_array(arr, start, end)
    quick_sort(arr, start, pivot - 1)
    quick_sort(arr, pivot + 1, end)
    return arr


if __name__ == '__main__':
    A = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    #print(partition_array(A, 0, len(A) - 1))
    print(quick_sort(A, 0, len(A) - 1))
