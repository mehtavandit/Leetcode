class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (-1,1), (1,-1)]

        if grid[0][0] !=0 or grid[rows-1][cols-1] != 0:
            return -1

        q = deque()
        q.append((0,0))
        grid[0][0] = 1

        while q:
            row, col = q.popleft()
            distance = grid[row][col]

            if (row, col) == (rows-1, cols-1):
                return distance
            
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 0:
                    grid[nr][nc] = distance + 1
                    q.append((nr, nc))

        return -1