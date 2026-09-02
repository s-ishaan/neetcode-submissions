class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return max(nums)

        def dp(arr):
            prev, curr = 0,0
            # n = len(arr)
            # dp = [0]*n
            # dp[1] = max(arr[0], arr[1])
            # dp[0] = arr[0]
            for num in arr:
                prev, curr = curr, max(num + prev, curr)

            return curr

        d1 = dp(nums[1:])
        d2 = dp(nums[:-1])                     
        return max(d1, d2)