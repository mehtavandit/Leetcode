class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        n = len(asteroids)
        # stack.append(asteroids[0])

        # for i in range(1, n):
        #     number1 = stack.pop()
        #     number2 = asteroids[i]

        #     result = number1 * number2
        #     if(result < 0):

        #         if abs(number1) < abs(number2):
        #             stack.append(number2)
        #         else:
        #             stack.append(number1)
                
        #     else:
        #         stack.append(number1)
        #         stack.append(number2)

        # number1 = stack.pop()
        # number2 = stack.pop()

        # result = number1 * number2
        # if(result < 0):
        #     if abs(number1) < abs(number2):
        #         stack.append(number2)
        #     else:
        #         stack.append(number1)
                
        # else:
        #     stack.append(number1)
        #     stack.append(number2)

        # return stack

        # for i in asteroids:
        #     stack.append(i)

        # if len(stack) == 2:
        #     number1 = stack.pop()
        #     number2 = stack.pop()

        #     if number1 + number2 == 0:
        #         return []

        # for i in range(n):

        #     if len(stack) >= 2:
        #         number1 = stack.pop()
        #         number2 = stack.pop()
        #         result = number1 * number2
        #         if result < 0:
        #             if abs(number1) < abs(number2):
        #                  stack.append(number2)
        #             else:
        #                 stack.append(number1)
        #         else:
        #             stack.append(number1)
        #             stack.append(number2)
                
        # return stack

        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return stack

            

            

            