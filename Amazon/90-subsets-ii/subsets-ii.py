class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            result.append(path[:])

            for i in range(start, len(nums)):
                if i>start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        nums.sort()
        backtrack(0, [])
        return result