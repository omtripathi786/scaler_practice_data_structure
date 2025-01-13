"""
Given two strings s and t, return true if t is an
anagram
 of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""
from collections import Counter


def solution(s, t):
    if len(s) != len(t):
        return False
    s_dict = Counter(s)
    t_dict = Counter(t)
    return s_dict == t_dict



if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(solution(s, t))
