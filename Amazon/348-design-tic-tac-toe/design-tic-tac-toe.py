class TicTacToe:

    # def __init__(self, n: int):
    #     self.n = n
    #     self.board = [[0]*n for _ in range(n) ]

    # def move(self, row: int, col: int, player: int) -> int:
    #     self.board[row][col] = player

    #     if self.check_row(row, player) or self.check_col(col, player) or (row == col and self.check_diagonal(player)) or (row == self.n - col - 1 and self.check_antidiagonal(player)):
    #         return player
        
    #     return 0

    # def check_row(self, row, player):
    #     for col in range(self.n):
    #         if self.board[row][col] != player:
    #             return False
    #     return True

    # def check_col(self, col, player):
    #     for row in range(self.n):
    #         if self.board[row][col] != player:
    #             return False
    #     return True

    # def check_diagonal(self, player):
    #     for i in range(self.n):
    #         if self.board[i][i] != player:
    #             return False
    #     return True

    # def check_antidiagonal(self, player):
    #     for i in range(self.n):
    #         if self.board[i][self.n-i-1] != player:
    #             return False
    #     return True

    #For every move we check each sell 4 times i.e O(4 * n) = O(n)
    #TC :- O(n2) for the board

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        current_player = 1 if player == 1 else -1

        self.rows[row] += current_player
        self.cols[col] += current_player

        if row == col:
            self.diagonal += current_player

        if col == self.n - row - 1:
            self.anti_diagonal += current_player

        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diagonal) == self.n or abs(self.anti_diagonal) == self.n:
            return player

        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)