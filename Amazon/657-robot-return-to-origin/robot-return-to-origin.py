class Solution:
    def judgeCircle(self, moves: str) -> bool:
        current_row = current_col = 0

        for i in moves:
            if i == "U":
                current_row -= 1
            if i == "D":
                current_row += 1
            if i== "L":
                current_col -= 1
            if i == "R":
                current_col += 1

        if current_row == 0 and current_col == 0:
            return True

        return False