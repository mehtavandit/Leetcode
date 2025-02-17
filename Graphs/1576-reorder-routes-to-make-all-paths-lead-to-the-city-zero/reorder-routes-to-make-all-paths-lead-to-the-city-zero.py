class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        forward_edges = defaultdict(list)
        backward_edges = defaultdict(list)

        for i,j in connections:
            forward_edges[i].append(j)
            backward_edges[j].append(i)


        print(forward_edges)
        print(backward_edges)

        def dfs(node, visited, edge):
            visited.add(node)

            for new_node in forward_edges[node]:
                if new_node not in visited:
                    edge[0] += 1
                    dfs(new_node, visited, edge)

            for new_node in backward_edges[node]:
                if new_node not in visited:
                    dfs(new_node, visited, edge)



        visited = set()
        edge = [0]
        dfs(0, visited, edge)
        return edge[0]