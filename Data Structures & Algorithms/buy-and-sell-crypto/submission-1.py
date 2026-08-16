class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_seen = prices[0]
        max_profit = 0
        for num in prices:
            min_seen = min(num, min_seen)
            max_profit = max(max_profit, num - min_seen)

        return max_profit