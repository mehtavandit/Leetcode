from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dictionary = defaultdict(list)
        result = []

        n = len(mat)
        m = len(mat[0])

        for i in range(n):
            for j in range(m):
                dictionary[i+j].append(mat[i][j])

        for item, values in dictionary.items():
            if item%2 == 0:
                length = len(values)
                for i in range(length-1, -1, -1):
                    result.append(values[i])
            else:
                length = len(values)
                for i in range(0, length):
                    result.append(values[i])
            

        return result

