from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        answer = float('inf')

        def dfs(node):
            nonlocal answer
            for neighbour, road_score in graph[node]:
                answer = min(answer, road_score)

                if not visited[neighbour]:
                    visited[neighbour] = True
                    dfs(neighbour)

        for src, dest, distance in roads:
            graph[src].append((dest, distance))
            graph[dest].append((src, distance))

        visited = [False] * (n+1)

        
        visited[1] = False
        dfs(1)

        return answer