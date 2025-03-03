class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xorr = nums[0]

        for i in range(1, len(nums)):
            xorr ^= nums[i]

        return xorr