class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        for i in range(n):
            if color[i] == -1:
                if not self.dfs(i, 0, graph, color):
                    return False
        return True

    def dfs(self, node, color_for_paint, graph, color):
        color[node] = color_for_paint

        for nei in graph[node]:
            if color[nei] == -1:
                if not self.dfs(nei, 1-color_for_paint, graph, color):
                    return False
            elif color[nei] == color_for_paint:
                return False

        return True