class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        left = 0
        right = len(self.events)

        while left < right:
            mid = (left + right) // 2

            if self.events[mid][0] < startTime:
                left = mid + 1
            else:
                right = mid

        
        if left > 0 and self.events[left-1][1] > startTime:
            return False

        if left < len(self.events) and self.events[left][0] < endTime:
            return False

        self.events.insert(left, (startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)