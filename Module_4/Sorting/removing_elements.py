"""
Problem Description
Given an integer array A of size N. You can remove any element from the array in one operation.
The cost of this operation is the sum of all elements in the array present before this operation.

Find the minimum cost to remove all elements from the array.
Problem Constraints
0 <= N <= 1000
1 <= A[i] <= 103

Input Format
First and only argument is an integer array A.

Output Format
Return an integer denoting the total cost of removing all elements from the array.

Example Input 1:
 A = [2, 1]
Input 2:
 A = [5]
Example Output 1:   4
Output 2:   5
"""


def remove_elements(arr):
    arr.sort(reverse=True)
    total_cost = 0
    for i in range(len(arr)):
        total_cost += A[i] * (i + 1)
    return total_cost


if __name__ == '__main__':
    A = [2, 1]
    print(remove_elements(A))
