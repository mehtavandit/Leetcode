class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        currentsum = nums[0]
        maxsum = nums[0]

        for i in range(1, n):
            currentsum = max(nums[i], currentsum + nums[i])
            maxsum = max(maxsum, currentsum)

        return maxsum