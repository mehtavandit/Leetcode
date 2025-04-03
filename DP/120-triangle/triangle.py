class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n = len(triangle)

        dp = [ [-1 for j in range(n)] for i in range(n)]
        
        def rec(row, col):
            if row == n-1:
                return triangle[n-1][col]

            if dp[row][col] != -1:
                return dp[row][col]

            down = triangle[row][col] + rec(row+1,col)
            dig = triangle[row][col] + rec(row+1,col+1)

            dp[row][col] = min(down, dig)
            return dp[row][col]



        return rec(0,0)