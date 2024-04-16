"""
Problem Description
Given an integer A pairs of parentheses, write a function to generate all
combinations of well-formed parentheses of length 2*A.

Problem Constraints
1 <= A <= 10
Input Format
First and only argument is integer A.
Output Format
Return a sorted list of all possible parenthesis.
Example Input 1: A = 3
Input 2: A = 1

Example Output
Output 1:
[ "((()))", "(()())", "(())()", "()(())", "()()()" ]
Output 2:
[ "()" ]
"""


def gen_parenth(n):
    ans = []

    def rec(n, s='', opening=0, closing=0):
        if len(s) == 2 * n:
            ans.append(s)
            return
        if opening < n:
            rec(n, s + '(', opening + 1, closing)
        if opening > closing:
            rec(n, s + ')', opening, closing + 1)
    rec(n,s='', opening=0, closing=0)
    return ans


if __name__ == '__main__':
    print(gen_parenth(3))
