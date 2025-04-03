class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])


        #Memoization
        # dp = [ [-1 for _ in range(cols)] for _ in range(rows)]



        # def rec(row, col):
        #     if row < 0 or col < 0:
        #         return float('inf')
            
        #     if row == 0 and col == 0:
        #         return grid[row][col]

        #     if dp[row][col] != -1:
        #         return dp[row][col]

        #     left = rec(row, col - 1) + grid[row][col]
        #     up = rec(row-1, col) + grid[row][col]

        #     dp[row][col] = min(left, up)
        #     return dp[row][col]


        # return rec(rows-1, cols-1)

        #Tabulation

        # dp = [ [-1 for _ in range(cols)] for _ in range(rows)]

        # dp[0][0] = grid[0][0]

        # for i in range(1, cols):
        #     dp[0][i] = dp[0][i-1] + grid[0][i]

        # for j in range(1, rows):
        #     dp[j][0] = dp[j-1][0] + grid[j][0]

        # for i in range(1, rows):
        #     for j in range(1, cols):
        #         dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])

        # return dp[rows-1][cols-1]

        #Space Optimize

        dp = [0] * cols

        dp[0] = grid[0][0]

        for j in range(1, cols):
            dp[j] = dp[j-1] + grid[0][j]

        for i in range(1, rows):
            dp[0] += grid[i][0]

            for j in range(1, cols):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]


        return dp[-1]
