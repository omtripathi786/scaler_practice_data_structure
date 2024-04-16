"""
Problem Description
In the classic problem of the Towers of Hanoi, you have 3 towers numbered from 1 to 3 (left to right)
and A disks numbered from 1 to A (top to bottom) of different sizes which can slide onto any tower.
The puzzle starts with disks sorted in ascending order of size
from top to bottom (i.e., each disk sits on top of an even larger one).
You have the following constraints:

Only one disk can be moved at a time.
A disk is slid off the top of one tower onto another tower.
A disk cannot be placed on top of a smaller disk.
You have to find the solution to the Tower of Hanoi problem.
You have to return a 2D array of dimensions M x 3, where M is the minimum number of moves needed to solve the problem.
In each row, there should be 3 integers (disk, start, end), where:

disk - number of the disk being moved
start - number of the tower from which the disk is being moved
end - number of the tower to which the disk is being moved


Problem Constraints
1 <= A <= 18


Input Format
The first argument is the integer A.


Output Format
Return a 2D array with dimensions M x 3 as mentioned above in the description.


Example
Input 1:
A = 2
Input 2:
A = 3

Example Output 1:
[1 1 2 ] [2 1 3 ] [1 2 3 ]
Output 2:
[1 1 3 ] [2 1 2 ] [1 3 2 ] [3 1 3 ] [1 2 1 ] [2 2 3 ] [1 1 3 ]
"""


def tower_of_hanoi(n):
    ans = []

    def rec(disk, start, end):
        l1 = [disk, start, end]
        if disk == 1:
            ans.append(l1)
            print(start, end)
            return
        mid = 6 - (start + end)
        rec(disk-1, start, mid)
        ans.append(l1)
        print(start, end)
        rec(disk - 1, mid, end)
    rec(n, 1, 3)
    return ans


if __name__ == '__main__':
    print(tower_of_hanoi(3))
