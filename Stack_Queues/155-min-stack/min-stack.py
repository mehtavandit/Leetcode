from queue import LifoQueue

class MinStack:

    def __init__(self):
        self.main_stack = LifoQueue()
        self.min_stack = LifoQueue()

    def push(self, val: int) -> None:
        self.main_stack.put(val)

        if(self.min_stack.qsize() == 0):
            self.min_stack.put(val)
        else:
            top_value = self.min_stack.queue[-1]
            if top_value < val:
                self.min_stack.put(top_value)
            else:
                self.min_stack.put(val)

    def pop(self) -> None:
        val1 = self.main_stack.get()
        val2 = self.min_stack.get()

    def top(self) -> int:
         return self.main_stack.queue[-1]

    def getMin(self) -> int:
        # val1 = self.main_stack.get()
        # val2 = self.min_stack.get()
        return self.min_stack.queue[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()