class Solution:
    def minSwaps(self, data: List[int]) -> int:
        count1 = data.count(1)
        total = 0

        for i in range(count1): #total of first window
            total += data[i]

        swaps = count1 - total

        for i in range(count1, len(data)):
            total += data[i]
            total -= data[i-count1]
            swaps = min(swaps, count1 - total)

        return swaps