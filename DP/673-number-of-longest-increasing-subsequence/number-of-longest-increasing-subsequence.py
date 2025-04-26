class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [1] * n
        count = [1] * n
        maximum = 1 

        for ind in range(n):
            for prev in range(ind):
                if nums[ind] > nums[prev] and 1 + dp[prev] > dp[ind]:
                    dp[ind] = dp[prev] + 1
                    count[ind] = count[prev]
                elif nums[ind] > nums[prev] and 1 + dp[prev] == dp[ind]:
                    count[ind] += count[prev]

            maximum = max(maximum, dp[ind])

        result = 0

        for i in range(n):
            if dp[i] == maximum:
                result += count[i]

        return result

        

        