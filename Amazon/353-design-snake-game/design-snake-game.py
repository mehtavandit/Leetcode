class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = deque()
        self.snake.append((0,0))
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0
        self.movement = {
            'U': [-1, 0],
            'D' : [1,0],
            'L' : [0, -1],
            'R' : [0, 1]
        }
        self.snake_set = {(0,0)}

    def move(self, direction: str) -> int:
        newHead = (self.snake[0][0] + self.movement[direction][0], self.snake[0][1] + self.movement[direction][1])

        if newHead[0] < 0 or newHead[0] >= self.height: #check if it goes out of height
            return -1

        if newHead[1] < 0 or newHead[1] >= self.width: #check if it goes out of widht
            return -1

        if newHead in self.snake_set and newHead != self.snake[-1]: #if it bites itself
            return -1

        new_food_item = self.food[self.food_index] if self.food_index < len(self.food) else None

        if new_food_item and newHead[0] == new_food_item[0] and newHead[1] == new_food_item[1]:
            self.food_index += 1
        else:
            tail = self.snake.pop()
            self.snake_set.remove(tail)

        self.snake.appendleft(newHead)
        self.snake_set.add(newHead)

        return len(self.snake) - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)