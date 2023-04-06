"""
Given an integer A, you need to find the count of it's factors.
Factor of a number is the number which divides it perfectly leaving no remainder.
Example : 1, 2, 3, 6 are factors of 6.

Problem Constraints
1 <= A <= 109
Time Complexity : O(√A)
Space Complexity : O(1)
"""

import math


def solve(A):
    count = 0
    sqt = int(math.sqrt(A))
    for i in range(1, sqt + 1):
        if A % i == 0:
            if i == A / i:
                count += 1
            else:
                count += 2
    return count


if __name__ == '__main__':
    print(solve(10))
