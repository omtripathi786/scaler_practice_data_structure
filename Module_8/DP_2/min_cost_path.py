"""
given a matrix Cost[m][n] with each cell representing cost, find the path with minimum cost to reach m,n from 0,0
At any instance, if you are on (x, y), you can either go to (x, y + 1) or (x + 1, y).
cost = [[1, 3, 5, 8], [4, 2, 1, 7], [4, 3, 2, 3]]
print(min_cost_path(cost))  # Output: 12
"""


def min_cost_path(cost):
    m, n = len(cost), len(cost[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = cost[0][0]
    # Initialize first rows
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + cost[i][0]
    # Initialize first cols
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + cost[0][j]
    # Fill the rest with the dp matrix
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + cost[i][j]
    return dp[m-1][n-1]


if __name__ == '__main__':
    cost = [
        [1, 3, 5, 8],
        [4, 2, 1, 7],
        [4, 3, 2, 3]
    ]
    print(min_cost_path(cost))
