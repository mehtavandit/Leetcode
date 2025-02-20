class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        n = len(s)

        result = [[] for _ in range(numRows)]

        current_row = 0
        going_down = False

        for char in s:
            result[current_row].append(char)

            if current_row == 0:
                going_down = True
            elif current_row == numRows - 1:
                going_down = False

            if going_down:
                current_row += 1
            else:
                current_row -= 1

        string = ""
        for i in result:
            for j in i:
                string += j

        return string