class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        counter = 1

        while counter <= n:
            for i in range(0, n-1):
                if nums[i] > nums[i+1]:
                    x = nums[i+1]
                    nums[i+1] = nums[i]
                    nums[i] = x

            counter += 1