class Node:
    def __init__(self, value = 0):
        self.value = value
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        # self.capacity = k
        # self.queue = [0] * k
        # self.front = 0
        # self.rear = -1
        # self.size = 0

        self.capacity = k
        self.size = 0
        self.front = None
        self.rear = None

    def enQueue(self, value: int) -> bool:
        # if self.isFull():
        #     return False
        # self.rear = (self.rear + 1) % self.capacity
        # self.queue[self.rear] = value
        # self.size += 1
        # return True

        if self.isFull():
            return False
        
        new_node = Node(value)

        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
            new_node.next = self.front #cirular link

        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front

        self.size += 1
        return True
    

    def deQueue(self) -> bool:
        # if self.isEmpty():
        #     return False
        # self.front = (self.front + 1) % self.capacity
        # self.size -= 1
        # return True

        if self.isEmpty():
            return False
        
        if self.size == 1:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

        self.size -= 1
        return True


    def Front(self) -> int:
        return -1 if self.isEmpty() else self.front.value


    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.rear.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()