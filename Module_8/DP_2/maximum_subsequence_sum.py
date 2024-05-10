"""
maximum subsequence sum in an array where adjacent element are not allowed
arr = [5, 5, 10, 40, 50, 35]
ans = 80
"""


def maximum_subseq_sum_rec(arr):
    n = len(arr)
    dp = [-1] * (n + 1)

    def _helper(arr, e):
        if e <= 0:
            return 0
        if dp[e] != -1:
            return dp[e]
        inc = arr[e - 1] + _helper(arr, e - 2)
        exc = _helper(arr, e - 1)
        dp[e] = max(inc, exc)
        return dp[e]

    return _helper(arr, n)


def maximum_subseq_sum_iter(arr):
    n = len(arr)
    dp = [-1] * n
    dp[0] = 0
    dp[1] = max(arr[0], arr[1])
    for i in range(2, n):
        dp[i] = max(arr[i] + dp[i - 2], dp[i-1])

    return dp[n-1]


if __name__ == '__main__':
    A = [5, 5, 10, 40, 50, 35]
    print(maximum_subseq_sum_rec(A))
    print(maximum_subseq_sum_iter(A))
