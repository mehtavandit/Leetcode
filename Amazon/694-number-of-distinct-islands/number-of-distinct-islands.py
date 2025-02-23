from collections import deque

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows= len(grid)
        cols = len(grid[0])

        visited = set()
        shapes = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(start_row, start_col):
            q = deque()
            shape = []
            q.append((start_row, start_col))
            visited.add((start_row, start_col))

            while q:
                row, col = q.popleft()
                shape.append((row - start_row, col - start_col))
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))

            return tuple(sorted(shape))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    shape = bfs(row, col)
                    print(shape)
                    shapes.add(shape)

        return len(shapes)