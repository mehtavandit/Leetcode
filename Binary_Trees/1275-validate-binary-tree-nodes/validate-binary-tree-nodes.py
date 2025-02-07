class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        parent = [-1] * n

        for i in range(n):
            if leftChild[i] != -1:
                if parent[leftChild[i]] != -1:
                    return False
                parent[leftChild[i]] = i

            
            if rightChild[i] != -1:
                if parent[rightChild[i]] != -1:
                    return False
                parent[rightChild[i]] = i

            
        root = -1
        for i in range(n):
            if parent[i] == -1:
                if root != -1:
                    return False
                root = i


        visited = set()
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()

            if node in visited:
                return False
            visited.add(node)
            if leftChild[node] != -1:
                stack.append(leftChild[node])
            if rightChild[node] != -1:
                stack.append(rightChild[node])

        

        return len(visited) == n