class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        candidates.sort()

        def rec(index, total, path):
            if total == target:
                result.append(path[:])
                return

            for i in range(index, len(candidates)):
                if i>index and candidates[i] == candidates[i-1]:
                    continue

                if total + candidates[i] > target:
                    break

                path.append(candidates[i])
                rec(i+1, total + candidates[i], path)
                path.pop()

        rec(0, 0, [])

        return result
