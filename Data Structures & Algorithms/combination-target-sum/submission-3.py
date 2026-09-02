class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol =[],[]
        n = len(nums)

        def backtracking(i, total):
            if i >= n or total > target:
                return
            
            if total == target:
                res.append(sol.copy())
                return

            #without i
            backtracking(i+1, total)

            #with i
            sol.append(nums[i])
            backtracking(i, total + nums[i])
            sol.pop()
        backtracking(0,0)
        return res
        