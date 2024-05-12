class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        longest = 1
        set_of_numbers = set()

        for i in nums:
            set_of_numbers.add(i)

        for i in set_of_numbers:
            
            if i-1 not in set_of_numbers:

                count = 1
                x = i

                while x+1 in set_of_numbers:
                    x += 1
                    count += 1

                longest = max(longest, count)

        return longest
