class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pool = set(nums)

        longest = 0

        for i in pool:
            if (i-1) not in pool:
                length = 1

                while (i+length) in pool:
                    length += 1

                longest = max(longest, length)

        return longest