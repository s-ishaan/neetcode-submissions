class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n= len(cost)
        memo = {0:0, 1:0} #step, cost
        
        def min_cost(k):
            if k in memo:
                return memo[k]
            if k not in memo:
                memo[k] = min(min_cost(k-1) + cost[k-1],
                                min_cost(k-2) + cost[k-2])
                return memo[k]


        return min_cost(n)