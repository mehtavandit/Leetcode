class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])

        for i in range(rows):
            for j in range(columns):
                if (matrix[i][j] == 0):
                    row_0 = i
                    col_0 = j

                    for k in range(columns):
                        if matrix[row_0][k] != 0:
                            matrix[row_0][k] = -999

                    for k in range(rows):
                        if matrix[k][col_0] != 0:
                            matrix[k][col_0] = -999

        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == -999:
                    matrix[i][j] = 0

                    