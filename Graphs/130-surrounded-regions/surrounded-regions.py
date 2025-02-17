from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def change_status():
            q = deque()

            
            for i in range(rows):  # Check every border 'O'
                for j in range(cols):
                    if board[i][j] == "O" and (i == 0 or j == 0 or i == rows - 1 or j == cols - 1):
                        q.append((i, j))  # Add border 'O' to the queue

            while q:
                row, col = q.popleft()

                if board[row][col] == "O":  # If it's an 'O', mark it
                    board[row][col] = "#"
                    for dr, dc in directions:
                        new_row, new_col = row + dr, col + dc
                        
                        if 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] == "O":
                            q.append((new_row, new_col))  # Add neighboring 'O' to the queue

       
        change_status()

        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X" 
                elif board[r][c] == "#":
                    board[r][c] = "O"  
