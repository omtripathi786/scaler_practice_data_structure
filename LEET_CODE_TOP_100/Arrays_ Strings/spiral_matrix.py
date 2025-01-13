"""
Given an m x n matrix, return all elements of the matrix in spiral order
Input: matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]
Output: [1,2,3,6,9,8,7,4,5]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


def solution(matrix):
    result = []
    m, n = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, m - 1, 0, n - 1
    while top <= bottom and left <= right:
        # traverse from left to right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        # traverse from top to bottom
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            # traverse from right to left
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            # traverse from bottom to top
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    return result


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solution(matrix))
