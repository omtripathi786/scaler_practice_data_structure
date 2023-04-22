"""
You are given an integer A. You have to tell whether it is a perfect number or not.
Perfect number is a positive integer which is equal to the sum of its proper positive divisors.
A proper divisor of a natural number is the divisor that is strictly less than the number.
Problem Constraints
1 <= A <= 106
"""


def solve(A):
    p_sum = 0
    for i in range(1, A // 2 + 1):
        if A % i == 0:
            p_sum += i
    if p_sum == A:
        return 1
    else:
        return 0


if __name__ == '__main__':
    print(solve(4))
