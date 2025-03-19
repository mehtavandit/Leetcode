import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        n = len(nums)

        for i in range(n):
            heapq.heappush(pq, -nums[i])

        while k > 1:
            heapq.heappop(pq)
            k -= 1

        return pq[0] * -1