class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])
        n = len(word)

        def dfs(i, j, k):
            if k == n:
                return True
            
            if (i < 0 or j < 0 or i >= rows or j >= columns or board[i][j] != word[k]):
                return False
            
            temp = board[i][j]
            board[i][j] = '#'
            
            found = (
                dfs(i + 1, j, k + 1) or
                dfs(i - 1, j, k + 1) or
                dfs(i, j + 1, k + 1) or
                dfs(i, j - 1, k + 1)
            )
            
            board[i][j] = temp
            return found

        for i in range(rows):
            for j in range(columns):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
                        
        return False