class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = 0
        m = len(matrix[0]) - 1

        while n < len(matrix) and m > -1:
            element = matrix[n][m]

            if element == target:
                return True

            elif element > target:
                m -= 1
            
            else:
                n += 1


