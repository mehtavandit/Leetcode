import heapq
class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.leftmost = []
        self.rightmost = 0

    def push(self, val: int) -> None:
        while self.leftmost and self.leftmost[0] < len(self.stacks) and len(self.stacks[self.leftmost[0]]) == self.capacity:
            heapq.heappop(self.leftmost)

        if not self.leftmost:
            self.stacks.append([])
            heapq.heappush(self.leftmost, len(self.stacks) - 1)

        index = heapq.heappop(self.leftmost)
        self.stacks[index].append(val)

        if len(self.stacks[index]) < self.capacity:
            heapq.heappush(self.leftmost, index)

        self.rightmost = max(self.rightmost, index)

    def pop(self) -> int:
        while self.rightmost >=0 and (self.rightmost >= len(self.stacks) or not self.stacks[self.rightmost]):
            self.rightmost -= 1

        if self.rightmost < 0:
            return -1

        val = self.stacks[self.rightmost].pop()

        heapq.heappush(self.leftmost, self.rightmost)

        return val

    def popAtStack(self, index: int) -> int:
        if index < len(self.stacks) and self.stacks[index]:
            val = self.stacks[index].pop()

            heapq.heappush(self.leftmost, index)

            return val
        
        return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)