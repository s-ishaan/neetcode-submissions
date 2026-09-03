class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<3:
            return max(nums)

        prev, curr = nums[0], max(nums[1], nums[0])
        for i in range(2,n):
            prev, curr = curr, max(curr, prev + nums[i])
        
        return curr

        
        