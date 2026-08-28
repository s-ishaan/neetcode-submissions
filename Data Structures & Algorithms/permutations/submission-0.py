class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(curr, i):
            if len(curr) == n:
                res.append(curr.copy())
                curr = []
                return
            if i ==n:
                return
            #for every number in nums, use it, dfs, discard
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    dfs(curr, i+1)
                    curr.pop()


            # skip it
            dfs(curr, i+1)


        dfs([], 0)
        return res