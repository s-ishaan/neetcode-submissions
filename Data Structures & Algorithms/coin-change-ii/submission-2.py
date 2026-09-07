class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = {} #(i, amount):#
        def dfs(i, amount):
            if amount == 0:
                return 1

            if (i, amount) in dp:
                return dp[(i,amount)]

            if i == len(coins) or amount<0:
                return 0

            skip = dfs(i+1, amount)
            take = dfs(i, amount-coins[i])

            dp[(i,amount)] = take + skip
            
            return dp[(i,amount)]


    
        return dfs(0, amount)