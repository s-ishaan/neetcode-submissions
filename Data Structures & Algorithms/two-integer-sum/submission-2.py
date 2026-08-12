class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need_dict = {}
        size = len(nums)
        for i in range(size):
            need = target - nums[i]
            if need in need_dict:
                return [need_dict[need], i]
            else:
                need_dict[nums[i]] = i