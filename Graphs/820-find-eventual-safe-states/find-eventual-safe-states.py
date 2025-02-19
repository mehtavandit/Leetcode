class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        status = {}

        def dfs(i):
            if i in status:
                return status[i]

            status[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            status[i] = True
            return True

        result = []
        for i in range(n):
            if dfs(i):
                result.append(i)

        return result

