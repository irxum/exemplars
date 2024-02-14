"""
Best Time to Buy and Sell Stock II
Medium

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of
the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to
achieve the maximum profit of 0.
"""

import logging

logging.basicConfig(level=logging.INFO)

class Solution:
    def find_max_trading_profit(self, trading_prices: list[float]) -> float:

        if not trading_prices:
            return 0
        
        if len(trading_prices) < 2:
            return 0
        
        profit = 0
        previous_price = trading_prices[0]

        for price in trading_prices[1:]:
            if price > previous_price:
                profit += price - previous_price
            previous_price = price

        return profit
    

sol = Solution()

test_inputs = [
    {
        "prices": [7,1,5,3,6,4],
        "max_profit": 7
    },
    {
        "prices": [1,2,3,4,5],
        "max_profit": 4
    },
    {
        "prices": [7,6,4,3,1],
        "max_profit": 0
    },
]

for test_input in test_inputs:
    prices = test_input["prices"]
    logging.info(prices)
    found_max_profit = sol.find_max_trading_profit(prices)
    logging.info(found_max_profit)
    expected = test_input["max_profit"]
    assert found_max_profit == expected, "something awry"
