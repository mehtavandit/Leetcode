class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)

        def rec(index, target, arr):
            if index == n or target == 0:
                if target == 0:
                    result.append(arr[:])
                return

            if candidates[index] <= target:
                arr.append(candidates[index])
                rec(index, target - candidates[index], arr)
                arr.pop()
            
            rec(index+1, target, arr)

        rec(0, target, [])

        return result
