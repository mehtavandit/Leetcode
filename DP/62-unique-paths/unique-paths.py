class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        rows = m
        cols = n

        #Memoization
        # dp = [ [-1 for _ in range(cols)] for _ in range(rows)]

        # print(dp)


        # def rec(row, col):
        #     if row == 0 or col == 0:
        #         return 1

        #     if dp[row][col] != -1:
        #         return dp[row][col]

        #     up = rec(row-1, col)
        #     left = rec(row, col - 1)

        #     dp[row][col] =  up + left
        #     return dp[row][col]

        # return rec(rows-1, cols-1)

        #Tabulation

        dp = [ [-1 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    dp[i][j] = 1

        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[rows-1][cols-1]
