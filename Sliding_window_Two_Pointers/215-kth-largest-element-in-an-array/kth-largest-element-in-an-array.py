import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        n = len(nums)

        for i in nums:
            heapq.heappush(pq, -i)

        f = k-1

        while f>0:
            heapq.heappop(pq)
            f -= 1

        return -pq[0]
