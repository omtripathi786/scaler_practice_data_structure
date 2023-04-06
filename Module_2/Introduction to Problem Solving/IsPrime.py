"""
Given an Integer A. Return 1 if A is prime and return 0 if not.
Problem Constraints
1 <= A <= 1012
Input 1:
A = 5
Input 2:
A = 10
Output 1:
1
Output 2:
0
"""
import math


def solve(A):
    count = 0
    sqt = int(math.sqrt(A))
    for i in range(1, sqt):
        if A % i == 0:
            if i == A / i:
                count += 1
            else:
                count += 2
    if count == 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    print(solve(4))
