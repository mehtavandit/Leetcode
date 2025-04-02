class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ans1 = self.helper(nums[1:])
        ans2 = self.helper(nums[:len(nums)-1])
        return max(ans1, ans2)

    def helper(self, nums):
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]

        dp = [-1] * n

        def rec(i):
            if i==0:
                return nums[0]
            if i<0:
                return 0
            if dp[i] != -1:
                return dp[i]
            pick = nums[i] + rec(i-2)
            notpick = 0 + rec(i-1)
            dp[i] =  max(pick, notpick)
            return dp[i]

        return rec(n-1)