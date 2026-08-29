class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        max_area = 0
        area = 0

        def dfs(i,j):
            if (i < 0 or i>=rows
                or j<0 or j>=columns
                or grid[i][j] != 1):
                return 0

            grid[i][j] = 0
            

            return 1 + (dfs(i+1, j) +
                        dfs(i-1, j) +
                        dfs(i, j+1) +
                        dfs(i, j-1))


        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i,j))

        return max_area