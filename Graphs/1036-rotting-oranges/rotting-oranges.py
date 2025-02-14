from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        fresh_orange = 0
        minutes = 0 

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_orange += 1
                if grid[i][j] == 2:
                    q.append((i,j))

        print(fresh_orange)
        print(q)

        if fresh_orange == 0:
            return 0

        while q:
            size = len(q)
            for i in range(size):
                row, col = q.popleft()

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    if 0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        q.append((new_row, new_col))
                        fresh_orange -= 1

            minutes += 1

        


        
        if fresh_orange == 0:
            return minutes - 1
        else:
            return -1