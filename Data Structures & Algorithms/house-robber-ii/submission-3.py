class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return max(nums)

        def dp(arr):
            n = len(arr)
            dp = [0]*n
            dp[1] = max(arr[0], arr[1])
            dp[0] = arr[0]
            for i in range(2,n):
                dp[i] = max(dp[i-1], arr[i] + dp[i-2])

            return dp[n-1]

        d1 = dp(nums[1:])
        d2 = dp(nums[:-1])                     
        return max(d1, d2)