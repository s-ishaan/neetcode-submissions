class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        start = []
        soln = 0
        for num in nums:
            if num-1 not in num_set:
                start.append(num)

        for item in start:
            counter = 1
            while(item + 1) in num_set:
                item = item+1
                counter += 1
            if counter > soln:
                soln = counter
        return soln
