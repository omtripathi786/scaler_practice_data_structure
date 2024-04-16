"""
Here we will do some basic questions on recursion like
1:- Fibonacci series
2:- Factorial
3:- Palindrome string
4:- Print 1 to A function
5:- sum of its digits
"""


def fibonacci_nth_term(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_nth_term(n - 1) + fibonacci_nth_term(n - 2)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def check_palindrome(A, s=0, e=None):
    if e is None:
        e = len(A) - 1
    if s >= e:
        return True
    if A[s] == A[e]:
        return check_palindrome(A, s + 1, e - 1)
    return False


def print1toA(A):
    if A == 0:
        return None
    print1toA(A - 1)
    print(A, end=' ')


def sum_of_digits(A):
    if A == 0:
        return 0
    return A % 10 + sum_of_digits(A // 10)


if __name__ == '__main__':
    print(fibonacci_nth_term(9))
    print(factorial(5))
    print(check_palindrome('naman'))
    print1toA(5)
    print('')
    print(sum_of_digits(46))
