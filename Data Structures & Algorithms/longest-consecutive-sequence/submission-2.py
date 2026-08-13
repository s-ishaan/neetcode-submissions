class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        soln = 0
        start = []
        set_num = set(nums)
        for num in nums:
            if num-1 not in set_num:
                start.append(num)

        for num in start:
            counter = 0
            while(num+1 in set_num):
                counter += 1
                num += 1
            if counter>soln:
                soln = counter

        return soln+1