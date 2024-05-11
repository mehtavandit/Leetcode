class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        xorr = 0

        for i in nums:
            xorr ^= i

        return xorr