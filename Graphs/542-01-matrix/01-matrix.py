from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        distances = [ [float('inf') for i in range(cols)] for j in range(rows)]

        

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    distances[i][j] = 0
                    q.append((i, j))

        print(distances)

        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0<=nr<rows and 0<=nc<cols and distances[nr][nc] > distances[row][col] + 1:
                    distances[nr][nc] = distances[row][col] + 1
                    q.append((nr, nc))

        return distances
