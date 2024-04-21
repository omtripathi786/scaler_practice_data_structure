"""
Problem Description
You are given an array A of N elements. Sort the given array in increasing
order of number of distinct factors of each element, i.e., element having the least
number of factors should be the first to be displayed and the number having highest
number of factors should be the last one. If 2 elements have same number of factors,
then number with less value should come first.

Note: You cannot use any extra space

Problem Constraints
1 <= N <= 104
1 <= A[i] <= 104

Input Format
First argument A is an array of integers.
Output Format
Return an array of integers.
Example Input 1:
A = [6, 8, 9]
Input 2:
A = [2, 4, 7]


Example Output 1:
[9, 6, 8]
Output 2:
[2, 7, 4]
"""


def count_factor(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


def costom_comparator(arr):
    sorted_number = sorted(arr, key=count_factor)
    return sorted_number


if __name__ == '__main__':
    A = [7, 13, 9, 12, 36, 16, 1]
    print(costom_comparator(A))
