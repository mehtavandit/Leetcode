class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            value = abs(num) - 1
            if nums[value] < 0:
                return abs(num)
            nums[value] *= -1

        return -1