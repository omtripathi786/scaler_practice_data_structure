"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product
of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space
for space complexity analysis.)
"""


def brute_force(nums):
    ans = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        ans.append(product)
    return ans


def solution(nums):
    n = len(nums)
    left_product = 1
    right_product = 1
    left_arr = [0] * n
    right_arr = [0] * n
    for i in range(n):
        j = -i - 1
        left_arr[i] = left_product
        right_arr[j] = right_product
        left_product *= nums[i]
        right_product *= nums[j]

    return [l * r for l, r in zip(left_arr, right_arr)]


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(brute_force(nums))
    print(solution(nums))
