from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]

        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = [False] * n

        def bfs(start):
            queue = deque([start])
            visited[start] = True
            while queue:
                node = queue.popleft()
                for nei in adj_list[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        queue.append(nei)


        count = 0
        for node in range(n):
            if visited[node] == False:
                bfs(node)
                count +=1

        return count