class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        # rows = len(obstacleGrid)
        # cols = len(obstacleGrid[0])

        #Memoization

        # if obstacleGrid[0][0] == 1 or obstacleGrid[rows-1][cols-1] == 1:
        #     return 0

        # dp = [[-1] * cols for _ in range(rows)]

        # def rec(row, col):
        #     if row < 0 or col < 0 or obstacleGrid[row][col] == 1:
        #         return 0

        #     if row==0 and col == 0:
        #         return 1

        #     if dp[row][col] != -1:
        #         return dp[row][col]

        #     up = rec(row-1,col)
        #     left = rec(row, col-1)

        #     dp[row][col] = up + left

        #     return dp[row][col]


        # return rec(rows-1, cols-1)

        #tabulation

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[rows-1][cols-1] == 1:
            return 0

        dp = [[0] * cols for _ in range(rows)]

        for j in range(cols):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
                break
            dp[0][j] = 1

        for i in range(rows):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                break
            dp[i][0] = 1

        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[rows-1][cols-1] if dp[rows-1][cols-1] != -1 else 0
 