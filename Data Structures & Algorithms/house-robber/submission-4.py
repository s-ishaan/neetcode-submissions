class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n)

        if n<3:
            return max(nums)

        for i in range(0, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[i]