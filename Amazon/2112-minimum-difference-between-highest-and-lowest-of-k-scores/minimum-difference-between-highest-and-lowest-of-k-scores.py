class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0

        nums.sort()

        min_diff = max(nums)

        for i in range(len(nums) - k+1):
            diff = abs(nums[i] - nums[i+k-1])
            min_diff = min(diff, min_diff)

        return min_diff