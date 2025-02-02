"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing
a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""


def brute_force(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            max_profit = max(max_profit, prices[j] - prices[i])
    return max_profit


def solution(prices):
    min_price = float("inf")
    max_profit = float("-inf")
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit


def max_sum(nums):
    curr_max = float('-inf')
    max_sum = float('-inf')
    for num in nums:
        curr_max = max(num, curr_max + num)
        max_sum = max(curr_max, max_sum)

    return max_sum


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(solution(prices))
    nums = [-2, 1, -3, 4, -1, 1, 1, -5, 4]
    print(max_sum(nums))
