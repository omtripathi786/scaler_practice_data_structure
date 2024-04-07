"""
Problem Description
Given a vector A of non-negative integers representing an elevation map,
where the width of each bar is 1, compute how much water it is able to trap after raining.

Problem Constraints
1 <= |A| <= 100000

Input Format
First and only argument is the vector A
Output Format
Return one integer, the answer to the question

Example Input
Input 1:
A = [0, 1, 0, 2]
Input 2:
A = [1, 2]
Example Output
Output 1:
1
Output 2:
0
Example Explanation
Explanation 1:
1 unit is trapped on top of the 3rd element.
Explanation 2:
No water is trapped.
"""


def water_trapped(arr):
    n, left, right = len(arr), 0, len(arr) - 1
    max_left, max_right, res = 0, 0, 0
    while left <= right:
        if A[left] <= A[right]:
            if A[left] >= max_left:
                max_left = A[left]
            else:
                res += max_left - A[left]
            left += 1
        else:
            if A[right] >= max_right:
                max_right = A[right]
            else:
                res += max_right - A[right]
            right -= 1

    return res


if __name__ == '__main__':
    A = [1, 0, 2, 5, 1, 0, 3, 0, 0, 7]
    print(water_trapped(A))
