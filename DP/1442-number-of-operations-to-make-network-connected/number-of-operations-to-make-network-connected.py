class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n


    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        self.components -= 1
        return True

class Solution:
    
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        dsu = DSU(n)
        extra_edges = 0

        for a, b in connections:
            if not dsu.union(a, b):
                extra_edges += 1

        if extra_edges >= dsu.components - 1:
            return dsu.components - 1
        else:
            return -1