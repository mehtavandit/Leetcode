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

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[n-1]