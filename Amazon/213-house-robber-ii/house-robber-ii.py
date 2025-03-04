# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]

#         return max((self.helper(nums[1:]), self.helper(nums[:-1]))) #you rob from house 1 to n and then house 0 to n-1, so that 0, and 1 doesn't coincides

#     def helper(self, nums):
#         if not nums:
#             return 0
        
#         if len(nums) == 1:
#             return nums[0]

#         dp = [0] * len(nums)

#         dp[0] = nums[0]

#         dp[1] = max(nums[0], nums[1])

#         for i in range(2, len(nums)):
#             dp[i] = max(dp[i-2] + nums[i], dp[i-1])

#         return dp[-1]

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # Case 1: Rob houses excluding the first house
        option1 = self.helper(nums[1:])
        
        # Case 2: Rob houses excluding the last house
        option2 = self.helper(nums[:-1])
        
        # Return the maximum of both options
        return max(option1, option2)
    
    def helper(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        prev2 = 0  # This represents dp[i-2]
        prev1 = nums[0]  # This represents dp[i-1]
        
        for i in range(1, len(nums)):
            current = max(prev1, nums[i] + prev2)  # dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            prev2 = prev1  # Update prev2 to be the previous prev1
            prev1 = current  # Update prev1 to be the current result
        
        return prev1
