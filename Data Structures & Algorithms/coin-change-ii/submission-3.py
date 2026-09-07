class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {} #(i, amount):#
        def dfs(i, amount):
            if amount == 0:
                return 1

            if (i, amount) in dp:
                return dp[(i,amount)]

            if i == len(coins) or amount<0:
                return 0

            dp[(i,amount)] = dfs(i+1, amount) + dfs(i, amount-coins[i])
            
            return dp[(i,amount)]


    
        return dfs(0, amount)