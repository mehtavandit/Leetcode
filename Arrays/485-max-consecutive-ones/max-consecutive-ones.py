class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_counter = 0
        local_counter = 0

        n = len(nums)

        for i in range(n):
            if nums[i] == 1:
                local_counter += 1
            else:
                if local_counter > max_counter:
                    max_counter = local_counter
                local_counter = 0

        if local_counter > max_counter:
            max_counter = local_counter
        
        return max_counter

        
