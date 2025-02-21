import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for (x, y) in points:
            dis = -(x*x + y*y) #bcoz python only supports min heap

            if len(heap) == k:
                heapq.heappushpop(heap, (dis, x,y))
            else:
                heapq.heappush(heap, (dis, x, y))

        return [(x,y) for (dis, x, y) in heap]