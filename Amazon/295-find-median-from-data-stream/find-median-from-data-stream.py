class MedianFinder:

    def __init__(self):
        self.numbers = []
        self.length = 0

    def addNum(self, num: int) -> None:
        self.numbers.append(num)
        self.length += 1

    def findMedian(self) -> float:
        self.numbers.sort()
        if self.length %2 == 0:
            middle_index = (self.length) // 2
            result = (self.numbers[middle_index-1] + self.numbers[middle_index]) / 2
            
        else:
            middle_index = (self.length) // 2
            result = self.numbers[middle_index]
        
        return result

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()