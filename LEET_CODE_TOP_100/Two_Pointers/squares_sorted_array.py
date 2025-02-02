"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares
of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""


def brute_force(nums):
    nums = [num ** 2 for num in nums]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] >= nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


def solution(nums):
    left = 0
    right = len(nums) - 1
    result = []
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result.append(nums[left] ** 2)
            left += 1
        else:
            result.append(nums[right] ** 2)
            right -= 1
    # result.reverse()
    left = 0
    right = len(result) - 1
    while left <= right:
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1
    return result


if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    # [0,1,9,16,100]
    print(brute_force(nums))
    print(solution(nums))
