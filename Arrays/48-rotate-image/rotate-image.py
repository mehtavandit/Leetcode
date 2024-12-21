class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(i, cols):
                x = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = x

        for i in range(rows):
            left = 0
            right = cols-1

            while left<right:
                x = matrix[i][left]
                matrix[i][left] = matrix[i][right]
                matrix[i][right] = x

                left += 1
                right-= 1

           
        