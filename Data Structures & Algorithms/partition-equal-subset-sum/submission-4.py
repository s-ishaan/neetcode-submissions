class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total%2 == 1:
            return False

        dp = [0]*n
        half = total/2
        for i in range(n):
            if nums[i] > half:
                return False
            s = 0
            for j in range(i,n):
                s = s+nums[j]            
                if s == half:
                    return True
                elif s > half:
                    s -= nums[j]
                

        return False