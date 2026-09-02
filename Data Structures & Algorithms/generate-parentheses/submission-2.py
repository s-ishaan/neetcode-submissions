class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sol = []

        def backtracking(openp, closep):
            if  openp > n or closep > openp:
                return

            if len(sol) == 2*n:
                res.append(''.join(sol.copy()))
                return
            
            sol.append('(')
            backtracking(openp + 1, closep)
            sol.pop()

            sol.append(')')
            backtracking(openp, closep + 1) 
            sol.pop()

        backtracking(0,0)
        return res