class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<3:
            return max(nums)

        def f(arr):
            prev, curr = 0,0
            for num in arr:
                prev, curr = curr, max(prev + num, curr)

            return curr
        
        return max(f(nums[1:]), f(nums[:-1]))