class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(city):
            for adjacent_city in range(n):
                if isConnected[city][adjacent_city] == 1 and not visited[adjacent_city]:
                    visited[adjacent_city] = True
                    dfs(adjacent_city)

        n = len(isConnected)

        visited = [False] * n
        province = 0

        for city in range(n):
            if not visited[city]:
                visited[city] = True
                province += 1
                dfs(city)

        return province
