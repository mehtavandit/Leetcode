class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def findSum(nums, goal):
            if goal < 0:
                return 0

            l = 0
            r = 0
            sum_ = 0
            count = 0
            n = len(nums)

            while (r<n):
                sum_ += nums[r]
                while (sum_ > goal):
                    sum_ -= nums[l]
                    l += 1
                count += r-l+1
                r += 1
            return count

        main_count = findSum(nums, goal) - findSum(nums, goal-1)
        return main_count

        
