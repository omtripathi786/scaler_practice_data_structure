"""
You will be given an integer n. You need to return the count of prime numbers less than or equal to n.
Problem Constraints
0 <= n <= 10^3
Input 1: 19
Input 2: 1
Output 1: 8
Output 2: 0
Explanation 1: Primes <= 19 are 2, 3, 5, 7, 11, 13, 17, 19
Explanation 2: There are no primes <= 1
"""
import math


def solve(A):
    count = 0
    for i in range(2, A+1):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
        if is_prime:
            count += 1
    return count


if __name__ == '__main__':
    print(solve(19))
