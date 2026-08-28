class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res , sol = [], []
        n = len(nums)

        def backtracking(i):
            if sum(sol) == target:
                res.append(sol[:])
                return
            if i == n or sum(sol) > target:
                return
            
            sol.append(nums[i])
            backtracking(i)
            sol.pop()

            backtracking(i+1)

        backtracking(0)
        return res
                