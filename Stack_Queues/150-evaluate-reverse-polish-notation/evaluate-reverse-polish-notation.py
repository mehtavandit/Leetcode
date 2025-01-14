from queue import LifoQueue

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = LifoQueue()

        operations = ['+', '-', '*', '/']

        for i in tokens:
            if i not in operations:
                stack.put(int(i))
            else:
                value1 = stack.get()
                value2 = stack.get()

                if i == "+":
                    result = value1 + value2
                elif i == "-":
                    result = value2 - value1
                elif i == "*":
                    result = value1 * value2
                else:
                    result = int(value2 / value1)

                stack.put(result)

        return stack.get()