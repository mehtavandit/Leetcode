import heapq

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # return len(set(nums) - {0})  

        min_heap = list(set(nums) - {0})

        heapq.heapify(min_heap)

        return len(min_heap)