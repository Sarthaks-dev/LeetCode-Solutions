class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        profit = 0
        for i in range (1,len(prices)):
            curr_prft = prices[i]-min_price
            if curr_prft>profit:
                profit = curr_prft
            min_price = min(min_price, prices[i])
        return profit