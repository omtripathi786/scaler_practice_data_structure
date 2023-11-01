"""
Problem Description
Given an array of integers A, find and return whether the
given array contains a non-empty subarray with a sum equal to 0.
If the given array contains a sub-array with sum zero return 1, else return 0.

Problem Constraints
1 <= |A| <= 100000
-10^9 <= A[i] <= 10^9

Input Format
The only argument given is the integer array A.
Output Format
Return whether the given array contains a subarray with a sum equal to 0.

Example Input
Input 1:
 A = [1, 2, 3, 4, 5]
Input 2:
 A = [4, -1, 1]
Example Output
Output 1:0
Output 2:1
"""


def solve(A):
    # Create a set to store cumulative sums
    cumulative_sum = set()
    current_sum = 0
    for num in A:
        current_sum += num
        # If the current sum is 0 or if it has been seen before, return 1
        if current_sum == 0 or current_sum in cumulative_sum:
            return 1
        # Add the current sum to the set
        cumulative_sum.add(current_sum)
    # If no subarray with sum 0 is found, return 0
    return 0


if __name__ == '__main__':
    A = [4, -1, 1]
    print(solve(A))
