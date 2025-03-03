class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxsum = float('-inf')

        for i in range(rows-2):
            for j in range(cols-2):
                sum_local = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]

                maxsum = max(sum_local, maxsum)

        return maxsum
