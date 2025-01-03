class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])-1

        for i in range(n):
            number = matrix[i][m]
            if number >= target:

                left = 0
                right = m

                while (left <= right):
                    mid = (left + right) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1

        return False

