from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)


        color = [-1] * (n+1)

        for i in range(1, n+1):
            if color[i] == -1:
                if not self.dfs(i,0, graph, color):
                    return False
        return True


    def dfs(self,node, color_for_paint,graph, color):
        color[node] = color_for_paint

        for nei in graph[node]:
            if color[nei] == -1:
                if not self.dfs(nei, 1-color_for_paint, graph, color):
                    return False
            elif color[nei] == color_for_paint:
                return False
        return True