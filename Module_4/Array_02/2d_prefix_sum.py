def prefix_sum(mat):
    rows = len(mat)
    cols = len(mat[0])
    ps = [[0] * cols for _ in range(rows)]
    print(ps)
    ps[0][0] = mat[0][0]
    for j in range(1, cols):
        ps[0][j] = ps[0][j - 1] + mat[0][j]
    for i in range(1, rows):
        ps[i][0] = ps[i - 1][0] + mat[i][0]

    for i in range(1, rows):
        for j in range(1, cols):
            ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + mat[i][j]

    print(ps)


def prefixMatrixSum(A):
    n = len(A)
    m = len(A[0])
    arr = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(m):
        arr[1][i + 1] = A[0][i]

        # Do column wise sum
    for i in range(1, n, 1):
        for j in range(0, m, 1):
            arr[i + 1][j + 1] = A[i][j] + arr[i][j + 1]

            # Do row wise sum
    for i in range(0, n, 1):
        for j in range(1, m, 1):
            arr[i + 1][j + 1] += arr[i + 1][j]

    return arr


if __name__ == '__main__':
    A = [
        [3, 4, 1],
        [6, 2, 9],
        [5, 3, 1]
    ]
    prefix_sum(A)
    print(prefixMatrixSum(A))
