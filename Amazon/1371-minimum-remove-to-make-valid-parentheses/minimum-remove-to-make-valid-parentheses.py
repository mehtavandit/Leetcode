class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        index_to_remove = set()
        stack = []

        for i, n in enumerate(s):
            if n not in "()":
                continue
            elif n == "(":
                stack.append(i)
            elif not stack:
                index_to_remove.add(i)
            else:
                stack.pop()


        index_to_remove = index_to_remove.union(set(stack))

        print(index_to_remove)

        result = []

        for i, n in enumerate(s):
            if i not in index_to_remove:
                result.append(n)

        print(result)

        return "".join(result)