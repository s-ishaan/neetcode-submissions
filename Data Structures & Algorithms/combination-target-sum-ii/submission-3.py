class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res, sol = [], []
        candidates.sort()

        def backtracking(i, total):
            if total == target:
                res.append(sol.copy())
                return
            if i >= n or total > target:
                return
            #with i
            sol.append(candidates[i])
            backtracking(i+1, total + candidates[i])
            sol.pop()

            #without i
            k = i
            while k+1 < n and candidates[k] == candidates[k+1]:
                k += 1
            backtracking(k+1, total)

        backtracking(0,0)
        return res