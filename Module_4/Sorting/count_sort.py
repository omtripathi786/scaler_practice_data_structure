
def count_sort(arr):
    min_ele, max_ele = min(arr), max(arr)
    freq = [0] * (max_ele - min_ele + 1)

    for num in arr:
        freq[num - min_ele] += 1
    print(freq)
    idx = 0
    for i in range(0, max_ele - min_ele + 1):
        for cnt in range(0, freq[i]):
            arr[idx] = i + min_ele
            idx += 1

    return arr


if __name__ == '__main__':
    A = [3, 2, 6, 1, 9, 7, 7]
    print(count_sort(A))
