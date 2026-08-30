class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        directions = [ (1,0),
                            (-1,0),
                            (0,1),
                            (0,-1)
                           ]

        res,sol =[],[]

        def adj(i,j):
            if (i<0 or j<0
                or i>=rows or j>=columns
                or grid[i][j] == '0'):
                return

            grid[i][j] = '0'
            for dx,dy in directions:
                nx = i+dx
                ny = j+dy

                adj(nx, ny)

            return 

        total = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    adj(i,j)
                    total+=1
        return total

            

            