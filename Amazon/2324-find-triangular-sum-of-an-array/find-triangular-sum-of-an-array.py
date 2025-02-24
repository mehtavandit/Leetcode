class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        while (len(nums) > 1):
            n = len(nums)
            temp_result = []
            for i in range(1, n):
                x = (nums[i] + nums[i-1]) % 10
                temp_result.append(x)
            
            nums = temp_result

        return nums[0]