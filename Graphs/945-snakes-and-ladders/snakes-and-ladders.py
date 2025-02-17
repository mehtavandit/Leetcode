from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        one_d = [-1] * (n * n) 

        index = 0

        for row in range(n-1, -1, -1):
            if (n-1-row) % 2 == 0:
                for col in range(n):
                    one_d[index] = board[row][col]
                    index += 1
            else:
                for col in range(n-1,-1,-1):
                    one_d[index] = board[row][col]
                    index += 1

        q = deque()
        q.append((0,0))
        visited = set()
        visited.add(0)

        while q:
            curr_pos, moves = q.popleft()

            for dice in range(1,7):
                new_pos = curr_pos + dice

                if new_pos >= n*n:
                    continue

                if one_d[new_pos] != -1:
                    new_pos = one_d[new_pos] -1

                if new_pos == n * n - 1:
                    return moves + 1

                if new_pos not in visited:
                    visited.add(new_pos)
                    q.append((new_pos, moves + 1))

        return -1