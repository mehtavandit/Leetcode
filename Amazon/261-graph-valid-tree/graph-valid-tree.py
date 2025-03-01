from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n)]

        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        queue = deque()
        queue.append((0,-1))
        visited = set()

        while queue:
            node, parent = queue.popleft()
            if node in visited:
                return False

            visited.add(node)

            for nei in adj_list[node]:
                if nei == parent:
                    continue
                queue.append((nei, node))
        
        return len(visited) == n