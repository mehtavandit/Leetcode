class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []


        for i in s:
            if i == "#" and stack1:
                stack1.pop()
            else:
                if i!="#":
                    stack1.append(i)

        for i in t:
            if i == "#" and stack2:
                stack2.pop()
            else:
                if i!="#":
                    stack2.append(i)

        print(stack1)

        print(stack2)

        return stack1 == stack2