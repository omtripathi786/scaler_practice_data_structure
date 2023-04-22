"""
Given an Aay A of N integers. Count the number of elements that have at least one elements greater than itself.
Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109
Input 1:
A = [3, 1, 2]
Input 2:
A = [5, 5, 3]
Output 1:
2
Output 2:
1
"""


def solve(A):
    max_count = 0
    max_elem = 0
    for x in A:
        if x == max_elem:
            max_count += 1
        elif x > max_elem:
            max_elem = x
            max_count = 1
    return len(A) - max_count


if __name__ == '__main__':
    print(solve([5, 5, 3]))
