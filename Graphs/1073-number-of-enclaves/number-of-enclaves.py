from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])


        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i == 0 or j == 0 or i == rows - 1 or j == cols-1):
                    q.append((i, j))
                    grid[i][j] = 0

        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                nr = dr + row
                nc = col + dc

                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    q.append((nr, nc))

        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count += 1

        return count