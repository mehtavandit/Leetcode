class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        rows = m
        cols = n

        dp = [ [-1 for _ in range(cols)] for _ in range(rows)]

        print(dp)


        def rec(row, col):
            if row == 0 or col == 0:
                return 1

            if dp[row][col] != -1:
                return dp[row][col]

            up = rec(row-1, col)
            left = rec(row, col - 1)

            dp[row][col] =  up + left
            return dp[row][col]

        return rec(rows-1, cols-1)