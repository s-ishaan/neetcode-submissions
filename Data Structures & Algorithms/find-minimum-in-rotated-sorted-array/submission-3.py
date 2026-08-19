class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        l = 0
        r = N-1

        while (l<r):
            m = l + ((r-l)//2)
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
            
        return nums[l]
