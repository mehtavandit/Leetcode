class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res1 = nums[0]
        max_ending = nums[0]

        for i in range(1, len(nums)):
            max_ending = max(max_ending + nums[i], nums[i])
            res1 = max(res1, max_ending)

        res2 = nums[0]
        min_ending = nums[0]

        for i in range(1, len(nums)):
            min_ending = min(min_ending + nums[i], nums[i])
            res2 = min(res2, min_ending)

        res2 = abs(res2)
        res1 = abs(res1)

        return res1 if res1>res2 else res2