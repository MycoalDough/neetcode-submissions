class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = -1

        for i in prices:
            if i < buy:
                buy = i
            else:
                profit = max(profit, i-buy)

        if profit < 0:
            return 0

        return profit
        