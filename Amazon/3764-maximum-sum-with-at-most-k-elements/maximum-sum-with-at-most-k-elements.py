import heapq

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        rows = len(grid)

        max_heap = []

        for i in range(rows):
            elements = sorted(grid[i], reverse = True)
            limit = limits[i]
            extacted_elements = elements[:limit]
            for num in extacted_elements:
                heapq.heappush(max_heap, -num)

        total = 0
        for i in range(k):
            total = total + (-heapq.heappop(max_heap))

        return total
