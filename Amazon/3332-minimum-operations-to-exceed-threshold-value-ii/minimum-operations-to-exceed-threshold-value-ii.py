import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_heap = []

        for i in range(len(nums)):
            heapq.heappush(min_heap, nums[i])

        counter = 0

        while min_heap[0] < k:
            counter += 1
            x = heapq.heappop(min_heap)
            y = heapq.heappop(min_heap)

            new_num = (min(x,y) * 2 + max(x,y))

            heapq.heappush(min_heap, new_num)
            

        return counter