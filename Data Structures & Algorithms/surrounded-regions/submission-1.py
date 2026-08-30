from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        columns = len(board[0])
        q = deque()
        safe = set()

        for i in range(rows):
            for j in range(columns):
                if (i ==0 or i == rows-1 or j ==0 or j==columns-1 ):
                    if board[i][j] == 'O':
                        q.append((i,j))
                        safe.add((i,j))

        directions = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]

        while q:
            x,y = q.popleft()
            for dx,dy in directions:
                nx = x + dx
                ny = y+dy

                if (nx<0 or ny<0
                    or nx>=rows or ny>=columns
                    or board[nx][ny] == 'X'
                    or (nx,ny) in safe):
                    continue
                safe.add((nx,ny))
                q.append((nx,ny))
        
        for i in range(rows):
            for j in range(columns):
                if (i,j) not in safe:
                    board[i][j] = 'X'