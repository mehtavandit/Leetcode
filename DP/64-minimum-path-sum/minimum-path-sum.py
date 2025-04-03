class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = [ [-1 for _ in range(cols)] for _ in range(rows)]



        def rec(row, col):
            if row < 0 or col < 0:
                return float('inf')
            
            if row == 0 and col == 0:
                return grid[row][col]

            if dp[row][col] != -1:
                return dp[row][col]

            left = rec(row, col - 1) + grid[row][col]
            up = rec(row-1, col) + grid[row][col]

            dp[row][col] = min(left, up)
            return dp[row][col]


        return rec(rows-1, cols-1)