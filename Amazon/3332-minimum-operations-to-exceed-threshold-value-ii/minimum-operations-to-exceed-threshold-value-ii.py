import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_heap = []

        for i in range(len(nums)): #inserting n elements into heap O(nlogn)
            heapq.heappush(min_heap, nums[i])

        counter = 0

        while min_heap[0] < k and len(min_heap) >= 2:
            counter += 1
            x = heapq.heappop(min_heap) #to take out element it is O(logn) and at worst you have to take out n elemets so O(nlogn)
            y = heapq.heappop(min_heap)

            new_num = (min(x,y) * 2 + max(x,y))

            heapq.heappush(min_heap, new_num)
            

        return counter