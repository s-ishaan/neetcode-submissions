class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*n
        dp[n-1] = True
        for j in range(n-2,-1,-1):
            if nums[j] == 0:
                dp[j] == False
            jump = False
            for i in range(nums[j]+1):
                jump = jump or dp[j+i]
            dp[j] = jump

        return dp[0]
                