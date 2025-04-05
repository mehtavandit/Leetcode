class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def rec(i, sub):
            if (i >= n):
                result.append(sub[:])
                return

            sub.append(nums[i])
            rec(i+1, sub)
            sub.pop()
            rec(i+1, sub)

        rec(0, [])

        return result