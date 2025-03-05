class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count1 = nums.count(1)

        if count1 == 0 or count1 == len(nums):
            return 0

        extended_arr = nums + nums
        total = sum(extended_arr[:count1]) #first window sum
        swaps = count1 - total

        for i in range(count1, len(nums) + count1):
            total += extended_arr[i]
            total -= extended_arr[i - count1]
            swaps = min(swaps, count1 -total)

        return swaps