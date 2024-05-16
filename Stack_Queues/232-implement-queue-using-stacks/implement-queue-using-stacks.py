from queue import LifoQueue

class MyQueue:

    def __init__(self):
        self.s1 = LifoQueue()
        self.s2 = LifoQueue()

    def push(self, x: int) -> None:
        
        while not self.s1.empty():
            self.s2.put(self.s1.get())

        self.s1.put(x)

        while not self.s2.empty():
            self.s1.put(self.s2.get())

    def pop(self) -> int:
        val = self.s1.get()
        return val

    def peek(self) -> int:
        return self.s1.queue[-1]

    def empty(self) -> bool:
        return self.s1.qsize() == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()