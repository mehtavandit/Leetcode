class Solution:
    def simplifyPath(self, path: str) -> str:
        path_arr = path.split("/")

        stack = []

        for element in path_arr:
            if element == "" or element == ".":
                continue

            if element == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(element)

        return "/" + "/".join(stack)