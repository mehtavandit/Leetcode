class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid1)
        cols = len(grid1[0])
        count = 0
        visited = set()

        def dfs(row,col):
            if (row < 0 or col < 0 or row == rows or col == cols or grid2[row][col] == 0 or (row, col) in visited):
                return True
            
            visited.add((row, col))
            res = True

            if grid1[row][col] == 0:
                res = False

            res = dfs(row-1, col) and res
            res = dfs(row + 1, col) and res
            res = dfs(row, col-1) and res
            res = dfs(row, col+1) and res

            return res

        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] and (i,j) not in visited and dfs(i,j):
                    count += 1

        return count