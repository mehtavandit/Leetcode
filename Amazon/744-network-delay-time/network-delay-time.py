from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u,v,w in times:
            adj[u].append((v, w))

        distance = {node:float('inf') for node in range(1, n+1)}
        
        def dfs(node, time):
            if time >= distance[node]:
                return
            
            distance[node] = time
            for nei, w in adj[node]:
                dfs(nei, time+w)

        dfs(k, 0)
        res = max(distance.values())
        return res if res!=float('inf') else -1