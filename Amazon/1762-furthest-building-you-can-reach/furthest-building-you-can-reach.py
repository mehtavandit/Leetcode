class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladders_use = []

        for i in range(len(heights) - 1):
            climb = heights[i+1] - heights[i]

            if climb <= 0:
                continue

            heapq.heappush(ladders_use, climb)

            if len(ladders_use) <= ladders:
                continue

            bricks -= heapq.heappop(ladders_use)

            if bricks < 0:
                return i

        return len(heights) -  1

