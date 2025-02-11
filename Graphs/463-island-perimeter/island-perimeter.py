class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        perimeter = 0

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 1:

                    current_perimeter = 4

                    for dx, dy in directions:
                        nx = i + dx
                        ny = j + dy

                        if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] == 1:
                            current_perimeter -= 1
                    
                    perimeter += current_perimeter

                
        return perimeter