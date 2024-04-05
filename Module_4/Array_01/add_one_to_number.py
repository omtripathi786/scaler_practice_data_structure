"""
Problem Description
Given a non-negative number represented as an array of digits, add 1 to the number
( increment the number represented by the digits ).
The digits are stored such that the most significant digit is at the head of the list.
NOTE: Certain things are intentionally left unclear in this question which you should practice
asking the interviewer. For example: for this problem, the following are some good questions to ask :

Q: Can the input have 0's before the most significant digit. Or, in other words, is 0 1 2 3 a valid input?
A: For the purpose of this question, YES
Q: Can the output have 0's before the most significant digit? Or, in other words, is 0 1 2 4 a valid output?
A: For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.

Problem Constraints
1 <= size of the array <= 1000000
Input Format
First argument is an array of digits.
Output Format
Return the array of digits after adding one.
Example Input 1: [1, 2, 3]
Example Output 1: [1, 2, 4]

Example Explanation 1:
Given vector is [1, 2, 3].
The returned vector should be [1, 2, 4] as 123 + 1 = 124.
"""


def add_one_to_number(digits):
    digits.reverse()
    carry = 1
    for i in range(len(digits)):
        digits[i] += carry
        if digits[i] > 9:
            digits[i] %= 10
            carry = 1
        else:
            carry = 0
    if carry == 1:
        digits.append(1)
    digits.reverse()
    # Remove leading zeros
    while len(digits) > 1 and digits[0] == 0:
        digits.pop(0)
    return digits


if __name__ == '__main__':
    A = [1, 2, 3]
    print(add_one_to_number(A))
