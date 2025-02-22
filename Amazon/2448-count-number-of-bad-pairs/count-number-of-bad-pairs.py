class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        good_count = 0
        n = len(nums)

        for i in range(n):
            diff = i - nums[i]
            if diff in freq:
                good_count += freq[diff]
            freq[diff] += 1

        total_pairs = (n * (n-1)) // 2
        return total_pairs - good_count