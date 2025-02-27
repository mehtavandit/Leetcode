class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            left_mid = nums[mid-1] if mid-1 >= 0 else float('-inf')
            right_mid = nums[mid + 1] if mid+1<len(nums) else float('-inf')

            if nums[mid] > left_mid and nums[mid] > right_mid:
                return mid
            elif nums[mid] < right_mid:
                left = mid + 1
            else:
                right = mid - 1

        return left

            