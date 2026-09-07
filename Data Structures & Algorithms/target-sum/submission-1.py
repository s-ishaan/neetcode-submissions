class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def dfs(i, amount):
            if i==n:
                if amount == target:
                    return 1
                return 0

            if (i, amount) in dp:
                return dp[(i, amount)]

            add = dfs(i+1, amount + nums[i])
            sub = dfs(i+1, amount - nums[i])

            dp[(i, amount)] = add + sub

            return dp[(i, amount)]

        return dfs(0,0)