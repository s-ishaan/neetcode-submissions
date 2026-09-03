class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}

        def calc(x):
            if x not in memo:
                memo[x] = calc(x-1) + calc(x-2)
            return memo[x]

        return calc(n)