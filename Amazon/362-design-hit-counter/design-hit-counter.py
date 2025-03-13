from collections import deque

class HitCounter:

    # def __init__(self):
    #     self.hits = deque()

    # def hit(self, timestamp: int) -> None: #O(1)
    #     self.hits.append(timestamp)

    # def getHits(self, timestamp: int) -> int: #O(n)
    #     while self.hits and self.hits[0] <= timestamp - 300:
    #         self.hits.popleft()

    #     return len(self.hits)

    #the above approach is not scalable when there are million hits per second bcoz sorting them is a time consuming process

    #To solve this use a circular array of size 300 (fixed size bucket)

    def __init__(self):
        self.size = 300
        self.time = [0] * self.size
        self.count = [0] * self.size


    def hit(self, timestamp: int) -> None: #O(1)
        index = timestamp % self.size

        if self.time[index] != timestamp:
            self.time[index] = timestamp
            self.count[index] = 1
        else:
            self.count[index] += 1

    def getHits(self, timestamp: int) -> int: #O(n)
        total_hits = 0
        for i in range(self.size):
            if timestamp - self.time[i] < self.size:
                total_hits += self.count[i]

        return total_hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)