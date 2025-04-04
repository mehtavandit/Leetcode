class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)

        dp = [ [-1 for _ in range(target+1)] for _ in range(n) ]

        # print(dp)

        def rec(index, target):
            if target == 0:
                return True

            if index == 0:
                return True if nums[index] == target else False

            if dp[index][target] != -1:
                return dp[index][target]

            notTake = rec(index - 1, target)
            take = False

            if nums[index] <= target:
                take = rec(index-1, target - nums[index])

            dp[index][target] = notTake or take
            return dp[index][target]

        return rec(n-1, total // 2)
