class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range(size):
            need = target - nums[i]
            for j in range(i+1, size):
                if nums[j] == need:
                    return [i,j]