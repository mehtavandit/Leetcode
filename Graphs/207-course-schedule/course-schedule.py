from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        result = []

        for i in prerequisites:
            adj[i[1]].append(i[0])

        
        indegrees = [0] * numCourses

        for nei in adj:
            for i in nei:
                indegrees[i] += 1

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
            return True

        return False


