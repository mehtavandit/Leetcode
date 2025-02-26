class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        candidates.sort()

        def dfs(index,path, total):
            if total == target:
                result.append(path[:])
                return

            if total > target:
                return

            for i in range(index, len(candidates)):
                path.append(candidates[i])
                dfs(i, path, total + candidates[i])
                path.pop()

        
        dfs(0, [], 0)
        return result