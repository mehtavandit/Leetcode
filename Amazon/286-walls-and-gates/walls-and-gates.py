class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        rows = len(rooms)
        cols = len(rooms[0])
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    q.append((i, j))

        while q:
            row, col = q.popleft()

            for nr, nc in directions:
                new_row = row + nr
                new_col = col + nc

                if 0<= new_row<rows and 0<=new_col<cols and rooms[new_row][new_col] > rooms[row][col] + 1 and rooms[new_row][new_col] != -1:
                    rooms[new_row][new_col] = rooms[row][col] + 1
                    q.append((new_row, new_col))

        print(rooms)
