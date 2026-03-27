# Problem: Best Time to Buy and Sell Stock III
# Language: python3
# Runtime: 68 ms
# Memory: 15.2 MB

from math import inf
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        t1_cost, t2_cost = inf, inf
        t1_profit, t2_profit = 0, 0

        for price in prices:
            # the maximum profit if only one transaction is allowed
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)
            # reinvest the gained profit in the second transaction
            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)

        return t2_profit