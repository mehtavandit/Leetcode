class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)

            else:
                if len(stack) == 0:
                    return False
                value = stack.pop()
                if i == ')' and value != '(':
                    return False

                if i == ']' and value != '[':
                    return False

                if i == '}' and value != '{':
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
            