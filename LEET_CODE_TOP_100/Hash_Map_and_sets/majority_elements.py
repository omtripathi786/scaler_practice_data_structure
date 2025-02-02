"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""


def brute_force(nums):
    counter = {}
    for num in nums:
        if num not in counter:
            counter[num] = 1
        else:
            counter[num] += 1

    max_count = float('-inf')
    ans = float('-inf')
    for key, value in counter.items():
        if value > max_count:
            max_count = value
            ans = key
    return ans


def solution(nums):
    count = 0
    ans = -1
    for num in nums:
        if count == 0:
            ans = num
        if ans == num:
            count += 1
        else:
            count -= 1
    return ans


if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(brute_force(nums))
    print(solution(nums))
