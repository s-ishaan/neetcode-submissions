from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        columns = len(grid[0])
        q = deque()

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] ==  0:
                    q.append((i,j))

        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]
        
        while q:
            x,y = q.popleft()

            for dx,dy in directions:
                nx = x + dx
                ny = y + dy

                if (nx < 0 or ny < 0
                    or nx >= rows or ny >= columns
                    or grid[nx][ny] != 2147483647):
                    continue
                
                grid[nx][ny] = grid[x][y] + 1
                q.append((nx,ny))

                

