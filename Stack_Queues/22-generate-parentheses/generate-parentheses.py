class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def paratheses(open_count, close_count):
            if open_count == close_count == n:
                result.append("".join(stack))

            if open_count < n:
                stack.append("(")
                paratheses(open_count+1, close_count)
                stack.pop()

            if close_count < open_count:
                stack.append(")")
                paratheses(open_count, close_count + 1)
                stack.pop()
            




        paratheses(0, 0)
        return result