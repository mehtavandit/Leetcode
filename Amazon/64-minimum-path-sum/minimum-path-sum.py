class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0]*n for _ in range(m)]

        dp[0][0] = grid[0][0]

        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]

        for j in range(1,m):
            dp[j][0] = dp[j-1][0] + grid[j][0]

        print(dp)

        for i in range(1,m):
            for j in range(1,n):
                left_sum, top_sum = 0,0
                if j>0:
                    left_sum = dp[i][j-1] + grid[i][j]
                if i>0:
                    top_sum = dp[i-1][j] + grid[i][j]
                dp[i][j] = min(left_sum, top_sum)

        return dp[m-1][n-1]