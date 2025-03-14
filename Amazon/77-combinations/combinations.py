class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(index, path):
            if len(path) == k:
                result.append(path[:])
                return

            if len(path) > k:
                return

            for i in range(index, n+1):
                path.append(i)
                dfs(i+1, path)
                path.pop()

        
        dfs(1, [])
        return result