from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = Counter(nums)

        # for num, freq in count.items():
        #     if freq > len(nums) // 2:
        #         return num

        nums.sort()  # Sort the array
        return nums[len(nums) // 2]