class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(n-2,-1,-1):
            final = nums[i]
            for j in range(i,n):
                if nums[j] > final:
                    dp[i] = max(1+dp[j], dp[i])
        return max(dp)

