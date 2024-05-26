class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        zeroes = 0
        maxlength = -999

        n = len(nums)

        while (r < n):
            if (nums[r] == 0):
                zeroes += 1
            while (zeroes > k):
                if (nums[l] == 0):
                    zeroes -= 1
                l += 1
            if (zeroes <= k):
                length = r-l+1
                maxlength = max(maxlength, length)
            r += 1

        return maxlength