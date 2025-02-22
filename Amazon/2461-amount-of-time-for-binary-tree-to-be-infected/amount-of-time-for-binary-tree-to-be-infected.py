# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        graph = defaultdict(list)

        def buildgraph(node, graph, parent = None):
            if not node:
                return

            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)

            if node.left:
                buildgraph(node.left, graph, node)

            if node.right:
                buildgraph(node.right, graph, node)
            
        
        buildgraph(root, graph)
        print(graph)

        q = deque()
        q.append(start)
        visited = set([start])

        minutes = -1

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

            minutes += 1


        return minutes