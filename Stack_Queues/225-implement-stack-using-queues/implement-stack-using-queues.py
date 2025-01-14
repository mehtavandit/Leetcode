import queue
class MyStack:

    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def push(self, x: int) -> None:
        self.q1.put(x)

    def pop(self) -> int:
        
        while (self.q1.qsize() > 1):
            self.q2.put(self.q1.get())

        x = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1
        return x
        

    def top(self) -> int:
        while(self.q1.qsize() > 1):
            self.q2.put(self.q1.get())

        x = self.q1.queue[0]
        self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1
        return x

    def empty(self) -> bool:
        return self.q1.qsize() == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()