class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # maxReach = 0

        # for i in range(len(nums)):
        #     if i > maxReach:
        #         return False
        #     maxReach = max(maxReach, i + nums[i])

        #     if maxReach >= len(nums) -1:
        #         return True

        # return True

        goal = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False