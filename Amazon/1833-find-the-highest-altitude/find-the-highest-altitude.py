class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        total_gain = [0] * len(gain)

        total_gain[0] = gain[0]

        for i in range(1, len(gain)):
            total_gain[i] = total_gain[i-1] + gain[i]

        result = max(total_gain)

        return result if result >= 0 else 0