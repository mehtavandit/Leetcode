class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack = []
        # n = len(asteroids)

        # for i in range(n):

        #     stack.append(asteroids[i])

        #     while len(stack) > 1 and stack[-1] * stack[-2] < 0:
        #         value1 = stack.pop()
        #         value2 = stack.pop()

        #         result = 0

        #         if abs(value1) > abs(value2):
        #             result = value1
        #         elif abs(value2) > abs(value1):
        #             result = value2
        #         else:
        #             continue
        #         stack.append(result)

        # return stack

        # Only positive asteroids can be damaged or destroyed because of the way they move

        stack = []

        for i in asteroids:
            while stack and stack[-1] > 0 and i < 0:
                if stack[-1] < -i:
                    stack.pop()
                    continue
                elif stack[-1] == -i:
                    stack.pop()
                break
            else:
                stack.append(i)

        return stack

