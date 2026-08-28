class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(curr):
            if len(curr) == n:
                res.append(curr.copy())
                curr = []
                return
            #for every number in nums, use it, dfs, discard
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    dfs(curr)
                    curr.pop()




        dfs([])
        return res