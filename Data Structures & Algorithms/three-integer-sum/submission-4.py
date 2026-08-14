class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        soln = []

        for n in range(len(nums)-2):
            if n > 0 and nums[n] == nums[n-1]:
                continue

            i = n+1
            j = len(nums) - 1
            need = -nums[n]  
            while (i<j):
                total = nums[i] + nums[j]
                if total == need:
                    soln.append([nums[i], nums[j], nums[n]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif total > need:
                    j -= 1
                else:
                    i += 1
        return soln
            