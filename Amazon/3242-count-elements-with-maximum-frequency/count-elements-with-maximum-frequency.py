class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq_counter = Counter(nums)

        max_freq = max(freq_counter.values())

        max_freq_elements = [num for num, freq in freq_counter.items() if freq == max_freq]

        return max_freq * len(max_freq_elements)