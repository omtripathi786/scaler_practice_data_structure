def fibonacci(n):
    """
    O(n) time complexity
    O(n) space complexity
    :param n:
    :return:
    """
    fib = [-1] * (n + 1)

    def _helper(n):
        if n <= 1:
            return n
        if fib[n] != -1:
            return fib[n]
        fib[n] = _helper(n - 1) + _helper(n - 2)
        return fib[n]

    return _helper(n)


def fibonacci1(n):
    """
    O(2^n) time complexity
    O(n) space complexity
    :param n:
    :return:
    """
    if n <= 1:
        return n
    return fibonacci1(n - 1) + fibonacci1(n - 2)


def fibonacci2(n):
    dp = [-1] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def fibonacci3(n):
    a, b = 0, 1
    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
    return c


if __name__ == '__main__':
    print(fibonacci(19))
    print(fibonacci1(19))
    print(fibonacci2(19))
    print(fibonacci3(19))
