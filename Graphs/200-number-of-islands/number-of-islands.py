from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(row, col):
            q = deque()
            q.append((row, col))
            visited.add((row, col))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == "1" and (new_row, new_col) not in visited:
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    islands += 1
                    bfs(i, j)

        return islands
