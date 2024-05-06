"""
Problem Description
Given an array of integers A of size N and an integer B.
The College library has N books. The ith book has A[i] number of pages.
You have to allocate books to B number of students so that the maximum number
of pages allocated to a student is minimum.

A book will be allocated to exactly one student.
Each student has to be allocated at least one book.
Allotment should be in contiguous order, for example: A student cannot be
allocated book 1 and book 3, skipping book 2.
Calculate and return that minimum possible number.

NOTE: Return -1 if a valid assignment is not possible.

Problem Constraints
1 <= N <= 105
1 <= A[i], B <= 105

Input Format
The first argument given is the integer array A.
The second argument given is the integer B.

Output Format
Return that minimum possible number.



Example Input
1:
A = [12, 34, 67, 90]
B = 2
Input 2:
A = [12, 15, 78]
B = 4
Example Output
1:
113
Output 2:
-1
"""


def max_number(A, B):
    n = len(A)
    n = len(A)
    if n < B:
        return -1
    low = max(A)
    high = sum(A)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if check(A, B, mid):
            high = mid - 1
            ans = mid
        else:
            low = mid + 1
    return ans


def check(A, B, mid):
    students_required = 1
    current_pages = 0
    for i in range(len(A)):
        if current_pages + A[i] > mid:
            current_pages = A[i]
            students_required += 1
            if students_required > B:
                return False
        else:
            current_pages += A[i]
    return True


if __name__ == '__main__':
    A = [97,26,12,67,10,33,79,49,79,21,67,72,93,36,85,45,28,91,94,57,1,53,8,44,68,90,24]
    B = 26
    print(max_number(A, B))
