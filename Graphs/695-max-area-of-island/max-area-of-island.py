from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        

        def bfs(row, col):
            print("Hello")
            q = deque()
            area = 0
            q.append((row, col))
            visited.add((row, col))

            while q:
                row, col = q.popleft()
                area += 1

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    if 0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))

            return area


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    area = bfs(i,j)
                    max_area = max(max_area, area)
                    print(max_area)

        return max_area