class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.buildGraph(equations, values)
        print(graph)
        result = []

        for query in queries:
            dividend, divisor = query

            if dividend not in graph or divisor not in graph:
                result.append(-1.0)
            else:
                visited = set()
                ans = [-1.0]
                temp = 1.0
                self.dfs(dividend, divisor, graph, visited, ans, temp)
                result.append(ans[0])

        return result

    def buildGraph(self, equations, values):
        graph = {}

        for i in range(len(equations)):
            dividend, divisor = equations[i]
            value = values[i]

            if dividend not in graph:
                graph[dividend] = {}
            if divisor not in graph:
                graph[divisor] = {}

            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1.0 / value

        return graph

    def dfs(self, dividend, divisor, graph, visited, ans, temp):
        if dividend in visited:
            return

        visited.add(dividend)

        if dividend == divisor:
            ans[0] = temp
            return
        
        for ne, val in graph[dividend].items():
            self.dfs(ne, divisor, graph, visited, ans, temp * val)