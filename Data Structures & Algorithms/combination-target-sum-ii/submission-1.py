class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        sol = []

        def backtracking(i, total):
            if total == target:
                res.append(sol.copy())
                return

            if i >= n or total > target:
                return

            # With candidates[i]
            sol.append(candidates[i])
            backtracking(i + 1, total + candidates[i])
            sol.pop()

            # Without candidates[i]:
            # skip all duplicates of candidates[i]
            k = i
            while k + 1 < n and candidates[k] == candidates[k + 1]:
                k += 1

            backtracking(k + 1, total)

        backtracking(0, 0)
        return res
