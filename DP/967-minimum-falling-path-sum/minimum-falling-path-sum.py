class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        min_value = float('inf')

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [ [-1 for _ in range(cols)] for _ in range(rows)]

        #Memoization
        # def rec(row, col):
        #     if col < 0 or col >= cols:
        #         return float('inf')

        #     if row == 0:
        #         return matrix[0][col]

        #     if dp[row][col] != -1:
        #         return dp[row][col]

        #     up = matrix[row][col] + rec(row-1, col)
        #     left_up = matrix[row][col] + rec(row-1, col-1)
        #     right_up = matrix[row][col] + rec(row-1, col+1)
            
        #     dp[row][col] =  min(up, left_up, right_up)
        #     return dp[row][col]


        # for j in range(cols):
        #     value = rec(rows-1, j)
        #     min_value = min(min_value, value)

        # return min_value

        #Tabulations

        # for j in range(cols):
        #     dp[0][j] = matrix[0][j]

        # print(dp)

        # for row in range(1, rows):
        #     for col in range(cols):
        #         up = dp[row-1][col] + matrix[row][col]
        #         left_up = dp[row-1][col-1] + matrix[row][col] if col > 0 else float('inf')
        #         right_up = dp[row-1][col+1] + matrix[row][col] if col < cols-1 else float('inf')

        #         dp[row][col] = min(up, left_up, right_up)


        # return min(dp[-1])

        #Space Optimized

        for row in range(1, rows):
            for col in range(cols):
                up = matrix[row-1][col] + matrix[row][col]
                left_up = matrix[row-1][col-1] + matrix[row][col] if col > 0 else float('inf')
                right_up = matrix[row-1][col+1] + matrix[row][col] if col < cols-1 else float('inf')

                matrix[row][col] = min(up, left_up, right_up)

        return min(matrix[-1])

