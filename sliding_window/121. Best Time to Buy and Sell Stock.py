class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        
        buy = prices[0]
        max_profit = 0

        for i in prices:
            if i < buy:
                buy = i
            max_profit = max(max_profit, i - buy)

        return max_profit


