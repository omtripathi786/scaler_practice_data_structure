"""
Problem Description
Given a number A. Return square root of the number if it is perfect square otherwise return -1.
Problem Constraints
1 <= A <= 108
Input Format
First and the only argument is an integer A.
Output Format
Return an integer which is the square root of A if A is perfect square otherwise return -1.
"""


def solve(A):
    # sqrt is the smallest integer less than equal to square root of A
    sqrt = int(A ** 0.5)
    if (sqrt * sqrt) == A:
        return sqrt
    return -1


if __name__ == '__main__':
    print(solve(5))
