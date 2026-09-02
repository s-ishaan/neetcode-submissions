class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])
        n = len(word)

        def dfs(i,j,target):
            if target == n:
                return True
            
            if (i >=rows or j>=columns
                or i<0 or j<0
                or board[i][j] != word[target]):
                return False
            
            temp = board[i][j]
            board[i][j] = '#'
            target += 1

            found =  (dfs(i+1,j, target) or
                        dfs(i-1,j, target) or
                        dfs(i,j+1, target) or
                        dfs(i,j-1, target))

            board[i][j] = temp
            return found

        for i in range(rows):
            for j in range(columns):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False
