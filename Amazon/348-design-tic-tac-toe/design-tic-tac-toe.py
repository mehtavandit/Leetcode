class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[0]*n for _ in range(n) ]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        if self.check_row(row, player) or self.check_col(col, player) or (row == col and self.check_diagonal(player)) or (row == self.n - col - 1 and self.check_antidiagonal(player)):
            return player
        
        return 0

    def check_row(self, row, player):
        for col in range(self.n):
            if self.board[row][col] != player:
                return False
        return True

    def check_col(self, col, player):
        for row in range(self.n):
            if self.board[row][col] != player:
                return False
        return True

    def check_diagonal(self, player):
        for i in range(self.n):
            if self.board[i][i] != player:
                return False
        return True

    def check_antidiagonal(self, player):
        for i in range(self.n):
            if self.board[i][self.n-i-1] != player:
                return False
        return True

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)