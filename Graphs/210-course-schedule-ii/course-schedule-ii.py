from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        result = []

        for j in prerequisites:
            adj[j[1]].append(j[0])
                

        indegrees =  [0] * numCourses

        for i in adj:
            for j in i:
                indegrees[j] += 1

        q = deque()

        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            result.append(node)

            for i in adj[node]:
                indegrees[i] -= 1

                if indegrees[i] == 0:
                    q.append(i)

        if len(result) == numCourses:
            return result
        return []