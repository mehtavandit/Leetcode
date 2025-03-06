import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []
        n = len(matrix)

        for i in range(n):
            heapq.heappush(min_heap, (matrix[i][0], i, 0))

        for _ in range(k-1):
            val, r, c = heapq.heappop(min_heap)

            if c + 1 < n :
                heapq.heappush(min_heap, (matrix[r][c+1],r,c+1))

        return heapq.heappop(min_heap)[0]