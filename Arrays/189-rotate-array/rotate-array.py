import math

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
    
        """


        n = len(nums)

        if n<=1:
            return

        k = k % n

        # for i in range(0, k):

        #     x = nums[n-1]

        #     for j in range(n-1, 0, -1):

        #         nums[j] = nums[j-1]

        #     nums[0] = x

        for i in range (0, floor(n/2)):

            x = nums[i]
            nums[i] = nums[n-i-1]
            nums[n-i-1] = x

        for i in range (0,floor(k/2)):
            x = nums[i]
            nums[i] = nums[k-i-1]
            nums[k-i-1] = x

        for i in range(0, floor((n-k)/2)):
            x = nums[i+k]
            nums[i+k] = nums[n-i-1]
            nums[n-i-1] = x 

        

        