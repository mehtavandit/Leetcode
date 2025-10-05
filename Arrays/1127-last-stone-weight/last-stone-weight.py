import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        heapq.heapify(h)

        for stone in stones:
            heapq.heappush(h, -1 * stone)

        while len(h) > 1:
            stone1 = -1 * heapq.heappop(h)
            stone2 = -1 * heapq.heappop(h)

            if stone1 == stone2:
                continue
            else:
                heapq.heappush(h, -1 * (stone1 - stone2))
        
        return -1 * heapq.heappop(h) if len(h) == 1 else 0
