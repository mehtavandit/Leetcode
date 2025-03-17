class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = []

        for i in sticks:
            heapq.heappush(heap, i)

        cost = 0
        
        while heap:
            number1 = heapq.heappop(heap)
            if not heap:
                return cost
            number2 = heapq.heappop(heap)

            cost += (number1 + number2)
            heapq.heappush(heap, (number1 + number2))

        return -1