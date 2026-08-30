from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        q = deque()

        directions = [
                    (1,0),
                    (0,1),
                    (-1,0),
                    (0,-1)
                    ]
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 2:
                    q.append((i,j))


        max_time = 0
        while q:
            x,y = q.popleft()
            for dx,dy in directions:
                nx = x+dx
                ny = y+dy

                if (
                    nx<0 or ny<0
                    or nx >=rows or ny>=columns
                    or grid[nx][ny] !=1
                    ):
                    continue
                grid[nx][ny] = grid[x][y] + 1
                max_time = max(max_time, grid[nx][ny])
                q.append((nx,ny))



        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    return -1
                    
        return max_time-2 if max_time>0 else 0
            
