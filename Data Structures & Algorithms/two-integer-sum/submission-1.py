class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        needs = {}
        for i in range(size):
            need = target - nums[i]
            if need in needs:
                return [needs[need], i]
            else:
                needs[nums[i]] = i