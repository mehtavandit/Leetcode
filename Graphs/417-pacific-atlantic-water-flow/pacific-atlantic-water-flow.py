from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(1,0),(-1,0), (0,1), (0,-1)]
        pacific_visited = set()
        atlantic_visited = set()
        result = []

        pacific_q = deque()
        atlantic_q = deque()

        for i in range(rows):
            for j in range(cols):
                if i==0 or j==0:
                    pacific_visited.add((i,j))
                    pacific_q.append((i,j))
                if i==rows-1 or j==cols-1:
                    atlantic_visited.add((i,j))
                    atlantic_q.append((i,j))

        def bfs(q, visited):
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()

                    for dr, dc in directions:
                        new_row = row + dr
                        new_col = col + dc

                        if 0<=new_row<rows and 0<=new_col<cols and (new_row, new_col) not in visited and heights[new_row][new_col] >= heights[row][col]:
                            q.append((new_row, new_col))
                            visited.add((new_row, new_col))




        bfs(pacific_q, pacific_visited)
        bfs(atlantic_q, atlantic_visited)

        intersections = pacific_visited & atlantic_visited

        result = [list(pair) for pair in intersections]

        return result
