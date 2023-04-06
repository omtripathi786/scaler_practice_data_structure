def solve(A, B):
    pre_fix_sum = [0] * len(A)
    for i in range(0, len(A)):
        if i % 2 == 0:
            pre_fix_sum[i] += A[i]
        else:
            pre_fix_sum[i] = A[i]
    print(pre_fix_sum)


if __name__ == '__main__':
    A = [16, 3, 3, 6, 7, 8, 17, 13, 7]
    B = [
        [2, 6],
        [4, 7],
        [6, 7]
    ]
    solve(A, B)
