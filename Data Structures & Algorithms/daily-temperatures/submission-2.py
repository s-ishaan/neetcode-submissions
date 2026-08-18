class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                pop = stack.pop()
                ans[pop[1]] = i - pop[1]
            
            stack.append([t,i])

        return ans