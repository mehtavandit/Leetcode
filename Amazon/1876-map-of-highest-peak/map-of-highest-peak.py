class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        cols = len(isWater[0])

        result = [ [float('inf')] * cols for _ in range(rows)]

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    result[i][j] = 0
                    q.append((i, j))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            row, col = q.popleft()

            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy

                if 0<=new_row<rows and 0<=new_col<cols and result[new_row][new_col] > result[row][col] + 1:
                    result[new_row][new_col] = result[row][col] + 1
                    q.append((new_row, new_col))

        return result

