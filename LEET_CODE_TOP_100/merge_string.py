"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other,
append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
"""

def merge(word1, word2):
    A, B = len(word1), len(word2)
    a, b = 0, 0
    s = []
    word = 1
    while a < B and b < A:
        if word == 1:
            s.append(word1[a])
            a += 1
            word = 2
        else:
            s.append(word2[b])
            b += 1
            word = 1
    while a < A:
        s.append(word1[a])
        a += 1
    while b < B:
        s.append(word2[b])
        b += 1
    return ''.join(s)

if __name__ == '__main__':
    word1 = "abc"
    word2 = "pqr"
    print(merge(word1, word2))
    word1 = "ab"
    word2 = "pqrs"
    print(merge(word1, word2))