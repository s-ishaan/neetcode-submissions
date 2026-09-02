class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        nums.sort()

        def backtracking(i):
            if i ==n:
                res.append(sol.copy())
                return

            #with i
            sol.append(nums[i])
            backtracking(i+1)
            sol.pop()

            #without i
            k = i
            while k+1<n and nums[k] == nums[k+1]:
                k+=1
            backtracking(k+1)

        backtracking(0)
        return res