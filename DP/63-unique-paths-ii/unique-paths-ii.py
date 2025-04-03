class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[rows-1][cols-1] == 1:
            return 0

        dp = [[-1] * cols for _ in range(rows)]

        def rec(row, col):
            if row < 0 or col < 0 or obstacleGrid[row][col] == 1:
                return 0

            if row==0 and col == 0:
                return 1

            if dp[row][col] != -1:
                return dp[row][col]

            up = rec(row-1,col)
            left = rec(row, col-1)

            dp[row][col] = up + left

            return dp[row][col]


        return rec(rows-1, cols-1)
