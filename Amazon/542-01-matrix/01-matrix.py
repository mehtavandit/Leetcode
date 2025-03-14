from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        distance = [[float('inf')] * cols for _ in range(rows)]

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    distance[i][j] = 0
                    q.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                if 0<=new_x<rows and 0<=new_y<cols:
                    if distance[new_x][new_y] > distance[x][y] + 1:
                        distance[new_x][new_y] = distance[x][y] + 1
                        q.append((new_x, new_y))

        return distance