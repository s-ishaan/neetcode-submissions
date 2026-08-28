class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def backtracking(total, i, sol):
            if total == target:
                res.append(sol.copy())
                return
            
            if total > target or i == n:
                return

            #include c[i]
            sol.append(candidates[i])
            backtracking(total + candidates[i], i+1, sol)
            sol.pop()

            #skip c[i]
            while i+1 < n and candidates[i] == candidates[i+1]:
                i += 1
            backtracking(total, i+1, sol)            

        backtracking(0, 0, [])
        return res