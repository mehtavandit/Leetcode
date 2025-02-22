class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        dp = [False] * (target + 1)

        dp[0] = True #Sum zero is always possible

        for num in nums:
            for j in range(target, num-1,-1): ## Traverse backwards to avoid reuse of the same number
                dp[j] = dp[j] or dp[j-num]

        return dp[target]
