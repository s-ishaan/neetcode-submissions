class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        def dfs(i, curr):
            if i == n:
                res.append(curr.copy())
                return

            
            #add the number check
            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()

            #skip this number
            while i+1<n and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, curr)

        dfs(0, [])
        return res