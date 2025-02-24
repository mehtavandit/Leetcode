class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        # while (len(nums) > 1):
        #     n = len(nums)
        #     temp_result = []
        #     for i in range(1, n):
        #         x = (nums[i] + nums[i-1]) % 10
        #         temp_result.append(x)
            
        #     nums = temp_result

        # return nums[0]

        n = len(nums)
        
        # Perform in-place transformation
        for i in range(n - 1):  # Run for (n-1) levels
            for j in range(n - 1 - i):  # Update only the relevant part
                nums[j] = (nums[j] + nums[j + 1]) % 10  # Modify in place

        return nums[0]  #