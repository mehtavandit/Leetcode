from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		visited = set()
        
        def bfs(start_node):
            queue = deque([(start_node, -1)]) 
            
            while queue:
                node, parent = queue.popleft()
                visited.add(node)
                
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, node))
                    elif neighbor != parent:
                        return True  
            return False
        
        
        for node in range(V):
            if node not in visited:
                if bfs(node):
                    return 1  
        return 0  
		


#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
