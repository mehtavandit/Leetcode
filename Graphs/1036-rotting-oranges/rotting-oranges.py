class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_oranges = 0
        minutes = 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_oranges +=1

        if fresh_oranges == 0:
            return 0

        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        while queue:
            minutes += 1
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for dx, dy in directions:
                    nx = x+dx
                    ny = y+dy

                    if 0 <= nx < rows and 0<=ny<cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_oranges = fresh_oranges - 1
                        queue.append((nx, ny))

        if fresh_oranges == 0:
            return minutes-1
        else:
            return -1