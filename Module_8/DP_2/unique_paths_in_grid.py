"""
Given a grid of size n * m, lets assume you are starting at (1,1) and your goal is to reach (n, m).
At any instance, if you are on (x, y), you can either go to (x, y + 1) or (x + 1, y).

Now consider if some obstacles are added to the grids.
Return the total number unique paths from (1, 1) to (n, m).

Note:
1. An obstacle is marked as 1 and empty space is marked 0 respectively in the grid.
2. Given Source Point and Destination points are 1-based index.


Problem Constraints
1 <= n, m <= 100
A[i][j] = 0 or 1


Input Format
Firts and only argument A is a 2D array of size n * m.


Output Format
Return an integer denoting the number of unique paths from (1, 1) to (n, m).


Example Input 1:

 A = [
        [0, 0, 0]
        [0, 1, 0]
        [0, 0, 0]
     ]
Input 2:

 A = [
        [0, 0, 0]
        [1, 1, 1]
        [0, 0, 0]
     ]


Example Output 1:
 2
Output 2:
 0


Example Explanation 1:

 Possible paths to reach (n, m): {(1, 1), (1, 2), (1, 3), (2, 3), (3, 3)} and {(1 ,1), (2, 1), (3, 1), (3, 2), (3, 3)}
 So, the total number of unique paths is 2.
Explanation 2:

 It is not possible to reach (n, m) from (1, 1). So, ans is 0.
"""


def unique_paths_rec(mat):
    n, m = len(mat), len(mat[0])
    dp = [[-1 for _ in range(m)] for _ in range(n)]

    def _helper(i, j):
        if i < 0 or j < 0 or mat[i][j] == 1:
            return 0
        if i == 0 or j == 0:
            return 1
        if dp[i][j] != -1:
            return dp[i][j]
        dp[i][j] = _helper(i, j - 1) + _helper(i - 1, j)
        return dp[i][j]

    return _helper(n - 1, m - 1)


def unique_paths_iter(mat):
    rows, cols = len(mat), len(mat[0])
    dp = [[-1] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if i == 0 or j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = dp[i][j - 1]
            elif j == 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[rows - 1][cols - 1]


if __name__ == '__main__':
    A = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    print(unique_paths_rec(A))
    print(unique_paths_iter(A))
